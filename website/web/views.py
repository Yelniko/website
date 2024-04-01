from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout



def home(request):
    return render(request, 'web/pages/code/home.html')


def teg(request):
    return render(request, 'web/pages/code/tasks.html')


@login_required()
def profile_view(request):
    return render(request, 'web/pages/code/home.html')


def logout_view(request):
    logout(request)
    return render(request, 'web/pages/code/home.html')




