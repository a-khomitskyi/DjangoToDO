from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<int:pk>', TaskDetail.as_view(), name='task_detail'),
    path('add-task/', TaskCreate.as_view(), name='create'),
    path('update-task/<int:pk>', TaskUpdate.as_view(), name='update'),
    path('delete-task/<int:pk>', TaskDelete.as_view(), name='delete'),
    path('action/<int:pk>', action, name='action'),
    path('drop-completed/', drop_all_completed, name='drop'),
    path('results/', TaskSearchView.as_view(), name='search'),
]
