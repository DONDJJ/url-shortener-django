from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import User
from django.views.generic import CreateView, ListView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.views import LoginView
from UrlShortenerApp.models import ShortenedUrl


class ProfileView(ListView):
    template_name = 'UserApp/profile.html'
    context_object_name = 'user_active_urls'

    def setup(self, request, *args, **kwargs):
        self.request = request

    def get_queryset(self):
        return ShortenedUrl.objects.filter(is_active=True, user_creator=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        context['current_user'] = self.request.user
        context['user_logged_in'] = self.request.user.is_authenticated
        return context


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


class HiddenUrlsView(ListView):
    template_name = 'UserApp/hidden_urls.html'
    context_object_name = 'user_inactive_urls'

    def setup(self, request, *args, **kwargs):
        self.request = request

    def get_queryset(self):
        return ShortenedUrl.objects.filter(is_active=False, user_creator=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        context['current_user'] = self.request.user
        context['user_logged_in'] = self.request.user.is_authenticated
        return context
