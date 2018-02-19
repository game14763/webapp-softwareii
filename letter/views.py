from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
import datetime
# Create your views here.

def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    login_form = LoginForm()
    regis_form = RegisterForm()
    return render(request, 'index.html', {'login_form': login_form, 'regis_form': regis_form})

def user_register(request):
    user = User.objects.create_user(username=request.POST['username'],
                                    email=request.POST['email'], 
                                    password=request.POST['password'])
    # user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    login(request, user)
    return redirect('/')

def user_login(request):
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return HttpResponse('<h1>Invalid Username or Password</h1>')

def user_logout(request):
    logout(request)
    return redirect('/')

