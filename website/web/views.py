from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic import FormView
from .forms import *
from .models import *


def home(request):
    return render(request, 'web/pages/code/home.html')


def teg(request):
    return render(request, 'registration/sing-up.html')


@login_required()
def profile_view(request):
    return render(request, 'web/pages/code/home.html')


@login_required()
def post(request):
    context = {
        'posts': Post.objects.filter(author=request.user)
    }
    return request(request, 'home.html', context)


def logout_view(request):
    logout(request)
    return render(request, 'web/pages/code/home.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/sing-up.html'
    success_url = 'accounts/profile/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
