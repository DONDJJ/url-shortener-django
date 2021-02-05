from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import User
from django.views.generic import CreateView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.views import LoginView
from UrlShortenerApp.models import ShortenedUrl


def profile_view(request):   # страница отображения активных ссылок
    appropriate_urls = ShortenedUrl.objects.filter(is_active=True, user_creator=request.user)
    return HttpResponse(render(request, 'UserApp/profile.html',
                               {'current_user': request.user, 'user_logged_in': request.user.is_authenticated,
                                "user_active_urls": appropriate_urls}))


class UserLoginView(LoginView):
    template_name = 'UserApp/login.html'
    form_class = LoginForm


class UserCreateView(CreateView):
    template_name = 'UserApp/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login_url')


def logout_view(request):
    logout(request)
    return redirect('login_url')


def hidden_urls_view(request):  # страница отображения неактивных ссылок
    appropriate_urls = ShortenedUrl.objects.filter(is_active=False, user_creator=request.user)
    return HttpResponse(render(request, 'UserApp/hidden_urls.html',
                               {'current_user': request.user, 'user_logged_in': request.user.is_authenticated,
                                "user_inactive_urls": appropriate_urls}))
