# Generated by Django 5.1 on 2024-08-13 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0006_alter_todo_deadline_alter_todo_finished_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="finished_at",
            field=models.DateField(null=True),
        ),
    ]
