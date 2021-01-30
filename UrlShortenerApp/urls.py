from django.urls import path
from .views import *
urlpatterns=[
    path('create_url', create_url_view, name="urlshortener_url")
]
