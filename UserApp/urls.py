from django.urls import path
from .views import *
from UrlShortenerApp.urls import urlpatterns
urlpatterns = [
    path('profile', ProfileView, name='profile_url'),
    path('login/', UserLoginView.as_view(), name='login_url'),
    path('registration/', UserCreateView.as_view(), name='registration_url'),
    path('logout/', logout_view, name='logout_url')
]
