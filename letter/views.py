from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from letter.models import Letter
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm, LetterForm
import datetime, time


def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    login_form = LoginForm()
    regis_form = RegisterForm()
    return render(request, 'index.html', {'login_form': login_form, 'regis_form': regis_form})

def user_register(request):
    user = User.objects.create_user(username=request.POST['regis_username'],
                                    email=request.POST['regis_email'],
                                    password=request.POST['regis_password'])
    login(request, user)
    return redirect('/')

def user_login(request):
    user = authenticate(request, username=request.POST['login_username'], password=request.POST['login_password'])
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return HttpResponse('<h1>Invalid Username or Password</h1>')

def user_logout(request):
    logout(request)
    return redirect('/')

def write_letter(request):
    if request.user.is_authenticated:
        letter_form = LetterForm()
        return render(request, 'write_letter.html', {'letter_form': letter_form})
    return redirect('/')

def send_letter(request):
    datetime_object = datetime.datetime.strptime(request.POST['datetime'], '%d/%m/%Y %H:%M')
    Letter.objects.create(subject=request.POST['subject'], message=request.POST['message'], datetime=datetime_object, user=request.user)
    return redirect('/')

def history(request):
    letter_list = Letter.objects.filter(user=request.user)
    return render(request, 'history.html', {'letter_list': letter_list})
