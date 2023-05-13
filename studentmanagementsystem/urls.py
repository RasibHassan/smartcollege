from django.urls import path
from .views import StudentList, student_details

urlpatterns = [
    path('students/', StudentList.as_view(), name='student-list'),
    path('students/<str:username>/', student_details, name='student_details'),
]