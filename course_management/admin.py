from django.contrib import admin

from .models import Payment, Schedule, School, Student, Subject


# Register your models here.
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Schedule)
admin.site.register(Payment)
