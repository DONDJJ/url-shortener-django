from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import User
from django.views.generic import CreateView, ListView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView
from UrlShortenerApp.models import ShortenedUrl
from django.template.defaulttags import register
from PetProject.settings import SITE_BASE_URL
from django.views.generic import TemplateView

@register.filter
def get_range(value):
    return range(1, value+1)


class ProfileView(ListView):
    template_name = 'UserApp/profile.html'
    context_object_name = 'user_active_urls'  # имя для QuerySet-a в шаблоне
    paginate_by = 10
    model = ShortenedUrl

    def setup(self, request, *args, **kwargs):
        super(ProfileView, self).setup(request)
        self.request = request

    def get_queryset(self):
        return ShortenedUrl.objects.filter(is_active=True, user_creator=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
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
    paginate_by = 10
    model = ShortenedUrl

    def setup(self, request, *args, **kwargs):
        super().setup(request)
        self.request = request

    def get_queryset(self):
        return ShortenedUrl.objects.filter(is_active=False, user_creator=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ResetPassword(PasswordResetView):
    template_name = 'UserApp/reset_password.html'
    subject_template_name = 'UserApp/email_template_subject.txt'  # тема письма
    html_email_template_name = 'UserApp/password_reset_email_body.html'
    success_url = reverse_lazy('password_reset_done')
    extra_email_context = {'SITE_BASE_URL':SITE_BASE_URL, }


class UserSettings(TemplateView):
    template_name = 'UserApp/user_settings.html'
