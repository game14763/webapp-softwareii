from django.contrib import admin
from django.urls import path

from letter import views

urlpatterns = [
    path('register', views.user_register, name='Register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('write/', views.write_letter, name='write letter'),
    path('send', views.send_letter, name='send letter'),
    path('history', views.history, name='history'),
]

