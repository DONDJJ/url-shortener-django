from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('create_url/', CreateUrlView.as_view(), name="urlshortener_url"),
    path('delete_url/<int:url_for_delete>', login_required(change_url_status_view, login_url='/user/login/'), name="urldelete_url"),
    path('stat/<int:url_for_stat>', login_required(statistic_about_url, login_url='/user/login/'), name='url_stat')
]
