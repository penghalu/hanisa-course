from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Subject


# Create your views here.
class SubjectList(LoginRequiredMixin, ListView):
    model = Subject
    context_object_name = 'subjects'
    template_name = 'course_management/subject_list.html'
    login_url = 'home'
