from django.urls import path

from users.views import UserList, UserAdd, UserDelete, UserUpdate

app_name = 'users'

urlpatterns = [
    path('', UserList.as_view(), name='list'),
    path('add/', UserAdd.as_view(), name='add'),
    path('edit/<int:pk>/', UserUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', UserDelete.as_view(), name='delete'),
]
