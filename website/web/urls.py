from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='home'),
    path('teg/', views.teg, name='task')
]

