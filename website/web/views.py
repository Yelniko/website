from django.shortcuts import render
from .models import *


def test(request):
    return render(request, 'web/pages/code/fist.html')


def teg(request):
    return render(request, 'web/pages/code/tasks.html')


