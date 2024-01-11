from django.shortcuts import render
from .models import *


def test(request):
    new = New.objects.all()
    return render(request, 'web/pages/code/home.html')


def teg(request):
    return render(request, 'web/pages/code/tasks.html')


