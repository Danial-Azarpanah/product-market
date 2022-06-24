from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout


# login view
def login_user(request):
    # redirect to home page if user is already logged in
    if request.user.is_authenticated:
        return redirect('home:main')

    # form processing
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home:main')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', context={'form': form})


# register view
def register_user(request):
    # redirect to home page if user is already logged in
    if request.user.is_authenticated:
        return redirect('home:main')

    # form processing
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data.get('username'),
                                            first_name=form.cleaned_data.get("first_name"),
                                            last_name=form.cleaned_data.get("last_name"),
                                            email=form.cleaned_data.get('email'),
                                            password=form.cleaned_data.get('password1'))
            user.save()
            login(request, user)
            return redirect('home:main')
    else:
        form = RegisterForm()

    return render(request, 'account/register.html', context={'form': form})


# logout view
def logout_user(request):
    logout(request)
    return redirect("home:main")
