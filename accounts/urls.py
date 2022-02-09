from django.urls import path
from accounts.views import UserRegister, UserLoginView, UserLogoutView


urlpatterns = [
    path('registration/', UserRegister.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
