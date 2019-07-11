from django.db import models

from djmoney.models.fields import MoneyField

from users.models import CustomUser


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=20, verbose_name='Subject')
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200, blank=True)
    grade = models.CharField(max_length=3)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, related_name='student', null=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    mentor = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='schedule')
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name='schedule')
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='schedule')
    payment = models.OneToOneField('Payment', on_delete=models.PROTECT, related_name='schedule')
    cost = MoneyField(max_digits=7, decimal_places=2, default_currency='IDR')
    description = models.CharField(max_length=200, verbose_name='Additional info', blank=True)
    schedule_start = models.DateTimeField()
    schedule_end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mentor.full_name


class Payment(models.Model):
    PAYMENT_STATUS = [
        ('Done', 'Done'),
        ('Waiting', 'Waiting'),
    ]

    status = models.CharField(max_length=7, choices=PAYMENT_STATUS, default='Waiting')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status
