from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/profile/', views.profile_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('registration', views.RegisterView.as_view(), name='sing-up'),
    path('create', views.create, name='create'),
    path('create/forum', views.create_forum, name='create_forum'),
    path('create/news', views.create_news, name='create_news'),
    path('<str:complexity>', views.task, name='task'),
    path('task/<int:question_id>/', views.task_description, name='description'),
    path('forum/', views.subject_forum, name='subject_forum'),
    path('forum/<str:subject>/', views.subject_post, name='posts'),
    path('about-us/', views.about_us, name='about'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('new/<int:new_id>/', views.new, name='new')
]
