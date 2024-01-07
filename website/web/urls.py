from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.test, name='home'),
    path('teg/', views.teg, name='teg')
]

