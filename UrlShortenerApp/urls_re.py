from django.urls import path, re_path
from .views import *

urlpatterns=[
    # re_path(r'short/\w{10}$',shorted_url_handler)
    re_path(r'^\w{10}$', shorted_url_handler)

]