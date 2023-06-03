from django.http import HttpResponse
from rest_framework import generics
from .models import Student,StudentData,Grades
from .serializers import StudentSerializer,StudentDetailsSerializer
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

def student_details(request, std_id):
    # Retrieve the Student object based on the provided username
    student = get_object_or_404(Student, std_id=std_id)

    # Retrieve the StudentDetails object associated with the Student
    student_details = StudentData.objects.filter(student=student)

    # Serialize the data to JSON and return it as a response
    print(student_details)
    data = []
    for data_obj in student_details:
        data.append({
            'course': data_obj.course.course_name,
            'total_attendance':40,
            'attendance': data_obj.attendance,
            'total_marks':20,
            'mid_marks': data_obj.marks,
            "semester": "Spring 2023",

        })
    return JsonResponse(data, safe=False)

def student_grades(request, std_id):
    # Retrieve the Student object based on the provided username
    student = get_object_or_404(Student, std_id=std_id)

    # Retrieve the StudentDetails object associated with the Student
    student_grades = get_object_or_404(Grades,student=student)
    data1=[{
        'cgpa':student_grades.cgpa,
        'gpa1':student_grades.gpa1,

        'gpa2':student_grades.gpa2,

        'gpa3':student_grades.gpa3,
        'gpa4':student_grades.gpa4,
    }]
    return JsonResponse(data1, safe=False)

