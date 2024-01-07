from django.shortcuts import render


def test(request):
    return render(request, 'web/pages/code/header.html')


def teg(request):
    return render(request, 'web/pages/code/teg.html')


