from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/profile/', views.profile_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('registration', views.RegisterView.as_view(), name='sing-up'),
    path('create', views.create, name='create'),
    path('task-easy', views.task_easy, name='task-easy'),
    path('task-medium', views.task_medium, name='task-medium'),
    path('task-hard', views.task_hard, name='task-hard')
]
