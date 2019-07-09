from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import School, Student, Subject


# Create your views here.
class SubjectList(LoginRequiredMixin, ListView):
    model = Subject
    context_object_name = 'subjects'
    template_name = 'course_management/subject_list.html'
    login_url = 'home'


class SubjectAdd(CreateView):
    model = Subject
    fields = '__all__'

    def get_success_url(self):
        return reverse('course_management:subject_list')


class SubjectUpdate(UpdateView):
    model = Subject
    fields = '__all__'

    def get_success_url(self):
        return reverse('course_management:subject_list')


class StudentList(LoginRequiredMixin, ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'course_management/student_list.html'
    login_url = 'home'


class StudentAdd(CreateView):
    model = Student
    template_name = 'course_management/student_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('course_management:student_list')


class StudentUpdate(UpdateView):
    model = Student
    fields = '__all__'

    def get_success_url(self):
        return reverse('course_management:student_list')


class StudentDelete(DeleteView):
    model = Student

    def get_success_url(self):
        return reverse('course_management:student_list')


class SchoolList(LoginRequiredMixin, ListView):
    model = School
    context_object_name = 'schools'
    login_url = 'home'


class SchoolAdd(CreateView):
    model = School
    fields = '__all__'

    def get_success_url(self):
        return reverse('course_management:school_list')


class SchoolUpdate(UpdateView):
    model = School
    fields = '__all__'

    def get_success_url(self):
        return reverse('course_management:school_list')


class SchoolDelete(DeleteView):
    model = School

    def get_success_url(self):
        return reverse('course_management:school_list')
