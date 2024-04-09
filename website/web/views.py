from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic import FormView
from .forms import *
from .models import *


def home(request):
    news = New.objects.order_by('-id')
    content = {
        'new': news
    }
    return render(request, 'web/pages/code/home.html', content)


def new(request, new_id):
    news = New.objects.get(id=new_id)
    content = {
        'new': news
    }
    return render(request, 'web/pages/code/new_all.html', content)


@login_required()
def cabinet(request):
    return render(request, 'web/pages/code/user.html')


def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'web/pages/code/create.html', context)


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


def create_forum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            form.save()

    form = ForumForm()
    context = {
        'form': form
    }
    return render(request, 'web/pages/code/create.html', context)


def create_news(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()

    form = NewForm()
    context = {
        'form': form
    }
    return render(request, 'web/pages/code/create.html', context)


def task(request, complexity):
    tasks = Task.objects.filter(complexity=complexity)
    content = {
        'task': tasks
    }
    return render(request, 'web/pages/code/task.html', content)


def task_description(request, question_id):
    tasks = Task.objects.get(id=question_id)
    content = {
        'task': tasks
    }
    return render(request, 'web/pages/code/task_description.html', content)


def subject_forum(request):
    subject = SubjectForum.objects.all()
    content = {
        'subject': subject
    }
    return render(request, 'web/pages/code/subjectforum.html', content)


def subject_post(request, subject):
    posts = Forum.objects.filter(subject=subject)
    content = {
        'post': posts
    }
    return render(request, 'web/pages/code/forumpost.html', content)


def about_us(request):
    return request(request, 'web/pages/code/about.html')
