from django.urls import path
from .views import *

urlpatterns = [
    path('create_url/', create_url_view, name="urlshortener_url"),
    path('delete_url/<int:url_for_delete>', delete_url_view, name="urldelete_url")
]
