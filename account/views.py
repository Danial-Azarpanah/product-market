from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy

from .forms import RegisterForm


class LoginUserView(LoginView):
    """
    Login user if username and password matches
    """
    template_name = 'account/login.html'
    redirect_authenticated_user = True
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('main:home')


class RegisterUserView(CreateView):
    """
    Create new user
    """
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('account:login')

    # Login to user right after registering
    def form_valid(self, form):
        form.save()  # Save the user first
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        return redirect('main:home')

    # Redirect the user to home page if already authenticated
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main:home')
        return super(RegisterUserView, self).get(*args, **kwargs)
