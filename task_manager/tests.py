from django.test import TestCase
from django.contrib.auth import authenticate
from task_manager.users.models import MyUser
from django import test


@test.modify_settings(
    MIDDLEWARE={
        "remove": [
            "rollbar.contrib.django.middleware.RollbarNotifierMiddleware",
        ]
    }
)
class IndexTest(TestCase):
    def setUp(self):
        self.user = MyUser.objects.create_user(
            username="test", password="12test12", first_name="bla", last_name="blabla"
        )
        self.user.save()

    def test_availability(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task_manager/index.html")

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username="test", password="12test12")
        self.assertTrue(user is not None and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username="wrong", password="12test12")
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username="test", password="wrong")
        self.assertFalse(user is not None and user.is_authenticated)
