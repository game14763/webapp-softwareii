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
    path('inbox', views.inbox, name='inbox'),
    path('detail', views.letter_detail, name='letter detail'),
    path('not_login', views.not_login, name='not login')
]

