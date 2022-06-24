from django import forms
from django.contrib.auth import authenticate
from django.forms import ValidationError
from django.contrib.auth.models import User


# The form for user login, with validation factors and limits
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'userame'}))
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))

    # Authenticate whether there is a matching user or not
    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is None:
            raise ValidationError('Username or password is wrong!', 'no_such_user')


# The form for user registration, with validation factors and limits
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'userame'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))

    first_name = forms.CharField(max_length=20,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}))

    last_name = forms.CharField(max_length=20,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}))

    password1 = forms.CharField(max_length=100,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))

    password2 = forms.CharField(max_length=100,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'confirm password'}))

    def clean(self):
        if self.cleaned_data.get('password1') == self.cleaned_data.get('password2'):  # If 2 passwords are the same
            if User.objects.filter(
                    username=self.cleaned_data.get('username')).exists():  # If this username is already taken
                raise ValidationError("Username already exists", "username_taken")
            elif User.objects.filter(email=self.cleaned_data.get('email')).exists():  # If this email is already taken
                raise ValidationError("Email already exists", "email_taken")
        else:  # If 2 passwords don't match
            raise ValidationError("Passwords don't match", "passwords_conflict")
