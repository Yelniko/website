# Generated by Django 5.0 on 2024-04-08 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
                ('post', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SubjectForum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
            ],
        ),
    ]
