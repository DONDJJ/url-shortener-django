from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import validators
from django.forms import ModelForm
from .models import User
from django import forms
from captcha.fields import CaptchaField

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


class UploadImageForm(forms.Form):
    captcha = CaptchaField(error_messages={'invalid':"Неправильный текст, попробуйте еще раз!"})
    new_profile_image = forms.ImageField(
        label="",
        validators=[validators.FileExtensionValidator(allowed_extensions=('jpg, png, jpeg, gif'))],
        error_messages={'invalid_extension': "Формат не поддерживается!"})

