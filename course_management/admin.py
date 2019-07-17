from django.contrib import admin

from .models import Schedule, School, Student, Subject


# Register your models here.
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Schedule)
