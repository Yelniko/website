from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    task_name = models.TextField(name='name')
    task_description = models.TextField(name='description')
    task_time = models.DateTimeField(auto_now_add=True)
    task_test = models.TextField(name='test')
    task_complexity = models.TextField(name='complexity')

    def __str__(self):
        return self.task_name


class New(models.Model):
    new_name = models.TextField(name='name')
    new_text = models.TextField(name='text')
    new_time = models.DateTimeField(auto_now_add=True)
    new_png = models.ImageField(upload_to='png/%Y/%n/')

    def __str__(self):
        return self.new_name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()



