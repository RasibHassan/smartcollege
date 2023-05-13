from django.http import HttpResponse
from rest_framework import generics
from .models import Student, StudentDetails
from .serializers import StudentSerializer, StudentDetailsSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

@require_http_methods(["GET"])
def student_details(request, username):
    # Retrieve the Student object based on the provided username
    student = get_object_or_404(Student, username=username)

    # Retrieve the StudentDetails object associated with the Student
    student_details = get_object_or_404(StudentDetails, student=student)

    # Serialize the data to JSON and return it as a response
    data = {
        'username': student.username,
        'department': student.department,
        'courses': student_details.courses,
        'attendance': student_details.attendance,
        'mid_marks': student_details.mid_marks,
    }
    return JsonResponse(data)