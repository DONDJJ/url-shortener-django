from django.urls import path
from .views import *
from UrlShortenerApp.urls import urlpatterns
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetDoneView

urlpatterns = [
    path('profile/', login_required(ProfileView.as_view()), name='profile_url'),
    path('user_settings', login_required(UserSettings.as_view()), name='user_settings'),
    path('login/', UserLoginView.as_view(), name='login_url'),
    path('registration/', UserCreateView.as_view(), name='registration_url'),
    path('logout/', login_required(logout_view), name='logout_url'),
    path('hidden/', login_required(HiddenUrlsView.as_view()), name='hidden_urls_url'),
    path('change_password', PasswordChangeView.as_view(template_name='UserApp/change_password.html',
                                                       success_url=reverse_lazy('password_change_done')),
                                                       name='change_password'),
    path('password_change_done', PasswordChangeDoneView.as_view(template_name='UserApp/change_password_done.html'),
         name='password_change_done'),
    path('reset_password', ResetPassword.as_view(), name='reset_password'),
    path('password_reset_done', PasswordResetDoneView.as_view(template_name='UserApp/password_reset_done.html'),
         name='password_reset_done')
    # TODO PasswordResetCompleteView и PasswordResetConfirm View
    # TODO починить отправку писем
]
