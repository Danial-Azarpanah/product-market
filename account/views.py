from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home:main')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home:main')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', context={'form': form})


def register_user(request):
    if request.user.is_authenticated:
        return redirect('home:main')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data.get('username'),
                                            email=form.cleaned_data.get('email'),
                                            password=form.cleaned_data.get('password1'))
            user.save()
            login(request, user)
            return redirect('home:main')
    else:
        form = RegisterForm()

    return render(request, 'account/register.html', context={'form': form})


def logout_user(request):
    logout(request)
    return redirect("home:main")
