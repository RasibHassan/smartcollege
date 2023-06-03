from django.urls import path
from .views import StudentList,student_details,student_grades

urlpatterns = [
    path('students/', StudentList.as_view(), name='student-list'),
    path('students/<int:std_id>/', student_details, name='student_details'),
    path('students/grades/<int:std_id>/', student_grades, name='student_grades'),

]