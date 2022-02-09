from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.conf import settings


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<int:pk>', TaskDetail.as_view(), name='task_detail'),
    path('registration/', UserRegister.as_view(), name='registration'),
    path('add-task/', TaskCreate.as_view(), name='create'),
    path('update-task/<int:pk>', TaskUpdate.as_view(), name='update'),
    path('delete-task/<int:pk>', TaskDelete.as_view(), name='delete'),
    path('action/<int:pk>', action, name='action'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('drop-completed/', drop_all_completed, name='drop'),
    path('results/', TaskSearchView.as_view(), name='search'),
]
