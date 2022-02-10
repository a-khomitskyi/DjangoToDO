from django.urls import path
from accounts.views import *
from django.contrib.auth.views import PasswordResetConfirmView
from accounts.forms import UserSetPasswordForm

urlpatterns = [
    path('registration/', UserRegister.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html',
                                          form_class=UserSetPasswordForm),
         name='password_reset_confirm'),
    path('password-reset-complete/', UserPasswordResetDone.as_view(), name='password_reset_complete'),
]
