from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):

    GENDER_OPTIONS = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    ROLE_OPTIONS = [
        ('Admin', 'Admin'),
        ('Mentor', 'Mentor'),
    ]

    full_name = models.CharField(max_length=50, verbose_name='Name')
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS, default='M')
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    description = models.CharField(max_length=200, verbose_name='Additional info', blank=True)
    role = models.CharField(max_length=6, choices=ROLE_OPTIONS, default='Mentor')

    def __str__(self):
        return self.username
