# Generated by Django 5.1.2 on 2024-10-21 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_tasks', '0002_task_priority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='title',
        ),
    ]
