from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.views.generic import CreateView, ListView

from .models import Student, Subject


# Create your views here.
class SubjectList(LoginRequiredMixin, ListView):
    model = Subject
    context_object_name = 'subjects'
    template_name = 'course_management/subject_list.html'
    login_url = 'home'


class SubjectAdd(CreateView):
    model = Subject
    template_name = 'course_management/subject_add.html'
    fields = [
        'name',
        'code'
    ]

    def get_success_url(self):
        return reverse('course_management:subject_list')


class StudentList(LoginRequiredMixin, ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'course_management/student_list.html'
    login_url = 'home'


class StudentAdd(CreateView):
    model = Student
    template_name = 'course_management/student_add.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('course_management:student_list')
