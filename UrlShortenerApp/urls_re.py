from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', create_url_view),  # обработка главной страницы, под адресом /
    re_path(r'^\w{10}$', shorted_url_handler)
]
