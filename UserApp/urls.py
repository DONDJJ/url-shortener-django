from django.urls import path
from .views import *
from UrlShortenerApp.urls import urlpatterns

urlpatterns = [
    path('profile', profile_view, name='profile_url'),
    path('login/', UserLoginView.as_view(), name='login_url'),
    path('registration/', UserCreateView.as_view(), name='registration_url'),
    path('logout/', logout_view, name='logout_url'),
    path('hidden/', hidden_urls_view, name='hidden_urls_url'),
]
