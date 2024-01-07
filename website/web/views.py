from django.shortcuts import render


def test(request):
    return render(request, 'web/pages/code_html/code/header.html')


def teg(request):
    return render(request, 'web/pages/code_html/code/teg.html')


