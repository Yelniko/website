from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('teg/', views.teg, name='task'),
    path('accounts/profile/', views.profile_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),

]

