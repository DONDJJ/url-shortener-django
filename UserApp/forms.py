from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm
from .models import User
from django import forms


class RegistrationForm(UserCreationForm):
    # username=forms.CharField(max_length=50)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
