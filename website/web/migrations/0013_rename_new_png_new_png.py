# Generated by Django 5.0 on 2024-04-09 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_rename_forum_time_forum_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='new_png',
            new_name='png',
        ),
    ]