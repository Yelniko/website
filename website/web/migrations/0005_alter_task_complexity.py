# Generated by Django 5.0 on 2024-04-03 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complexity',
            field=models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], max_length=6),
        ),
    ]
