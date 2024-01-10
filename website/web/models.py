from django.db import models


class User(models.Model):
    user_name = models.TextField(name='name')
    user_email = models.TextField(name='email')
    user_password = models.TextField(name='password')


class Task(models.Model):
    task_name = models.TextField(name='name')
    task_description = models.TextField(name='description')
    task_time = models.DateTimeField(name='time')
    task_test = models.TextField(name='test')


class New(models.Model):
    new_name = models.TextField(name='name')
    new_text = models.TextField(name='text')
    new_time = models.DateTimeField(name='time')
    new_png = models.TextField(name='png')

