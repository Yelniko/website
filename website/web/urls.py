from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/profile/', views.profile_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('registration', views.RegisterView.as_view(), name='sing-up'),
    path('create', views.create, name='create'),
    path('<str:complexity>', views.task, name='task'),
    path('task/<int:question_id>/', views.task_description, name='description')
]
