# Generated by Django 5.0 on 2024-04-09 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_new'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forum',
            old_name='forum_time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='new',
            old_name='new_time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_time',
            new_name='time',
        ),
    ]
