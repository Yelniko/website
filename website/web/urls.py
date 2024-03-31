from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.test, name='home'),
    path('teg/', views.teg, name='task'),
    path('accounts/profile/', views.profile_view, name='login'),

]

