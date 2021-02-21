from django.urls import path, re_path
from .views import *
from UrlShortenerApp.urls import urlpatterns
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

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

    path('password_reset/', ResetPassword.as_view(), name='password_reset'),  # страница с вводом почты
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='UserApp/password_reset_done.html'),
         name='password_reset_done'),  # сообщение "письмо было отправлено на почту"

    # ссылка из письма
    path('password_reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='UserApp/reset_new_passwords.html'), name='password_reset_confirm'),

    # после введения нового пароля
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='UserApp/reset_password_complete.html'), name='password_reset_complete')
]
