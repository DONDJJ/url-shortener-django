from django.urls import path
from .views import *
from UrlShortenerApp.urls import urlpatterns
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('profile/', login_required(ProfileView.as_view(), login_url='/user/login/'), name='profile_url'),
    path('login/', UserLoginView.as_view(), name='login_url'),
    path('registration/', UserCreateView.as_view(), name='registration_url'),
    path('logout/', login_required(logout_view, login_url='/user/login/'), name='logout_url'),
    path('hidden/', login_required(HiddenUrlsView.as_view(), login_url='/user/login/'), name='hidden_urls_url'),
]
