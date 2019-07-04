from django.shortcuts import render
from django.views.generic import ListView

from .models import CustomUser


# Create your views here.
class UserList(ListView):
    model = CustomUser
    template_name = 'users/list.html'
    context_object_name = 'users'
