from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator

from .models import CustomUser


# Create your views here.
class UserList(ListView):
    model = CustomUser
    template_name = 'users/list.html'
    context_object_name = 'users'


@method_decorator(staff_member_required, name='dispatch')
class UserAdd(CreateView):
    model = CustomUser
    template_name = 'users/add.html'
    fields = [
        'role',
        'full_name',
        'email',
        'username',
        'password',
        'gender',
        'address',
        'phone',
        'description'
    ]

    def get_success_url(self):
        return reverse('users:list')
