from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import validators
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


class UploadImageForm(forms.Form):
    new_profile_image = forms.ImageField(
        label="",
        validators=[validators.FileExtensionValidator(allowed_extensions=('jpg, png, jpeg, gif'))],
        error_messages={'invalid_extension': "Формат не поддерживается!"})

    def __init__(self):
        super().__init__()
        self.fields['new_profile_image'].widget.attrs \
            .update({
            # 'class': "btn btn-danger",
            # 'id':'inputGroupFile01',
            # 'aria-describedby':'inputGroupFileAddon01',
        })
