from django.urls import path
from .views import StudentList,student_details,student_grades,TeacherList,Teacher_details,student_fees,student_exam

urlpatterns = [
    path('students/', StudentList.as_view(), name='student-list'),
    path('students/<int:std_id>/', student_details, name='student_details'),
    path('students/grades/<int:std_id>/', student_grades, name='student_grades'),
    path('teachers/', TeacherList.as_view(), name='techer-list'),
    path('teachers/<int:t_id>/', Teacher_details, name='student_details'),
    path('students/fees/<int:std_id>/', student_fees, name='student-list'),
    path('students/exam/<int:std_id>/', student_exam, name='student-list'),

]