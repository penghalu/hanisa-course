from django.urls import path

from .views import SchoolAdd, SchoolDelete, SchoolList, SchoolUpdate, SubjectAdd, SubjectList, StudentAdd, StudentList


app_name = 'course_management'

urlpatterns = [
    path('subjects/', SubjectList.as_view(), name='subject_list'),
    path('subjects/add/', SubjectAdd.as_view(), name='subject_add'),
    path('students/', StudentList.as_view(), name='student_list'),
    path('students/add/', StudentAdd.as_view(), name='student_add'),
    path('schools/', SchoolList.as_view(), name='school_list'),
    path('schools/add/', SchoolAdd.as_view(), name='school_add'),
    path('schools/edit/<int:pk>/', SchoolUpdate.as_view(), name='school_update'),
    path('schools/delete/<int:pk>/', SchoolDelete.as_view(), name='school_delete'),
]
