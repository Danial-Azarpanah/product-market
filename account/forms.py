from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    """
    Registration form for new and unregistered users
    """
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'Last name'}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Email'}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                  'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                  'placeholder': 'Repeat Password'}))

    # Save user's info to User built-in model with the fields specified
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

    def clean(self):

        # Show error if the new username is already taken
        if User.objects.filter(username=self.cleaned_data.get('username')).exists():
            raise ValidationError('Username already taken!', 'username_taken')

        elif User.objects.filter(email=self.cleaned_data.get('email')).exists():
            raise ValidationError('Email already taken!', 'email_taken')
