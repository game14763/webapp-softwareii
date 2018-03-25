from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from letter.models import Letter
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm, LetterForm
from django.utils import timezone


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
    user = authenticate(request, username=request.POST['login_username'], 
            password=request.POST['login_password'])
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return HttpResponse('<h1>Invalid Username or Password</h1>')

def user_logout(request):
    logout(request)
    return redirect('/')

def not_login(request):
    login_form = LoginForm()
    regis_form = RegisterForm()
    return render(request, 'not_login.html',
            {'login_form': login_form, 'regis_form': regis_form})

def write_letter(request):
    if request.user.is_anonymous:
        return redirect('/letter/not_login')
    letter_form = LetterForm()
    return render(request, 'write_letter.html', {'letter_form': letter_form})

def send_letter(request):
    datetime_object = timezone.datetime.strptime(request.POST['datetime'], '%d/%m/%Y %H:%M')
    if request.POST['to'] is None or request.POST['to'] == '':
        Letter.objects.create(subject=request.POST['subject'], 
                              message=request.POST['message'], 
                              destination_time=datetime_object, 
                              user=request.user,
                              reciever=request.user
                              )
    else:
        Letter.objects.create(subject=request.POST['subject'],
                              message=request.POST['message'],
                              destination_time=datetime_object,
                              user=request.user,
                              reciever=User.objects.get(username=request.POST['to'])
                              )
    return redirect('/')

def history(request):
    if request.user.is_anonymous:
        return redirect('/letter/not_login')
    letter_list = Letter.objects.filter(user=request.user)
    return render(request, 'history.html', {'letter_list': letter_list})

def inbox(request):

    if request.user.is_anonymous:
        return redirect('/letter/not_login')

    letter_list = Letter.objects.filter(reciever=request.user,
            destination_time__lte=timezone.now())
    return render(request, 'inbox.html', {'letter_list': letter_list})

def letter_detail(request):
    if request.user.is_anonymous:
        return redirect('/letter/not_login')
    letter = Letter.objects.get(pk=request.POST['letter_id'])
    letter.status = 'Read'
    letter.save(update_fields=["status"])
    return render(request, 'detail.html', {'letter': letter})
