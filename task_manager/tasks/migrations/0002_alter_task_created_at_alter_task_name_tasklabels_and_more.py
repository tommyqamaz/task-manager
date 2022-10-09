# Generated by Django 4.1.2 on 2022-10-09 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("labels", "0002_alter_label_name"),
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Creation date"),
        ),
        migrations.AlterField(
            model_name="task",
            name="name",
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.CreateModel(
            name="TaskLabels",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "label",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="labels.label"
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tasks.task"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="task",
            name="label",
            field=models.ManyToManyField(through="tasks.TaskLabels", to="labels.label"),
        ),
    ]