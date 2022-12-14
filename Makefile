MANAGE := poetry run python manage.py
PK?=1
TEST_APP?=task_manager

.PHONY: test
test:
	@poetry run pytest

.PHONY: setup
setup: db-clean install migrate

.PHONY: install
install:
	@poetry install --no-root

.PHONY: db-clean
db-clean:
	@rm db.sqlite3 || true

.PHONY: migrate
migrate:
	@$(MANAGE) makemigrations && $(MANAGE) migrate

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython

.PHONY: lint
lint:
	@poetry run flake8 task_manager

.PHONY: run
run:
	$(MANAGE) runserver 8001

run-g:
	@poetry run gunicorn task_manager.wsgi

heroku:
	@poetry export > requirements.txt && git push heroku main
	
.PHONY: test
test:
	@$(MANAGE) test $(TEST_APP)

test-coverage:
	@poetry run coverage run --source='.' manage.py test && poetry run coverage xml

create-user:
	@poetry run python manage.py dumpdata users.MyUser --pk $(PK) --indent 4 > user.json