# Generated by Django 4.2.18 on 2025-01-30 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_task_delete_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
