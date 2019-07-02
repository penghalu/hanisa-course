from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('full_name', 'gender', 'address', 'phone', 'description', 'role')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
