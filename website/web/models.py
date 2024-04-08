from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    task_name = models.TextField(name='name')
    task_description = models.TextField(name='description')
    task_time = models.DateTimeField(auto_now_add=True)
    task_input = models.TextField(name='input')
    task_output = models.TextField(name='output')
    task_complexity = models.CharField(name='complexity', max_length=6, choices=(('easy', 'easy'),
                                                                                 ('medium', 'medium'),
                                                                                 ('hard', 'hard')))


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


class SubjectForum(models.Model):
    subject = models.TextField(name='subject')


class Forum(models.Model):
    forum_subject = models.TextField(name='subject')
    forum_post = models.TextField(name='post')
