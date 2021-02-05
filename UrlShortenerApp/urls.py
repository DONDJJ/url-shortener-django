from django.urls import path
from .views import *

urlpatterns = [
    path('create_url/', create_url_view, name="urlshortener_url"),
    path('delete_url/<int:url_for_delete>', change_url_status_view, name="urldelete_url"),
    path('stat/<int:url_for_stat>', statistic_about_url, name='url_stat')
]
