from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.conf import settings


urlpatterns = [
    path('', index),
    path('test/', HomeView.as_view()),
]
