from django.http import HttpResponse
from rest_framework import generics
from .models import Student,StudentData,Grades,Teacher,FEES,Examination
from .serializers import StudentSerializer,StudentDetailsSerializer,TeacherSerializer,FeesSerializer
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
        percentage=(data_obj.attendance/40)*100
        data.append({
            'course': data_obj.course.course_name,
            'attendance_percentage':percentage,
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
    data1=[
    {
        "grade": "GPA",

        "gpa1": student_grades.gpa1

    },
    {
        "grade": "GPA2",

        "gpa2": student_grades.gpa2

    },
    {
        "grade": "GPA3",

        "gpa3": student_grades.gpa3

    },  {
        "grade": "GPA4",

        "gpa4": student_grades.gpa4

    },
    {
        "grade": "CGPA",

        "cgpa": student_grades.cgpa

    },
    ]
    

    return JsonResponse(data1, safe=False)
class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
def Teacher_details(request, t_id):
    # Retrieve the Student object based on the provided username
    teacher = get_object_or_404(Teacher,teacher_id=t_id)

    student_details = Student.objects.filter(courses__course_id=teacher.course.course_id)

    data = []
    for data_obj in student_details:
        data.append({
            "std_id":data_obj.std_id,
            "username":data_obj.username

        })
    return JsonResponse(data, safe=False)
def student_fees(request, std_id):
    # Retrieve the Student object based on the provided username
    student = get_object_or_404(Student, std_id=std_id)

    # Retrieve the StudentDetails object associated with the Student
    student_fee = get_object_or_404(FEES,student=student)
    data=[{
        "amount":student_fee.ammount,
        "status":student_fee.status
    }]
    return JsonResponse(data, safe=False)
def student_exam(request, std_id):
    # Retrieve the Student object based on the provided username
    student = get_object_or_404(Student, std_id=std_id)
    courses = student.courses.all()

    student_ex = Examination.objects.filter(course__in=courses)
    data = []
    for data_obj in student_ex:
        data.append({
            "coursename":data_obj.course.course_name,
            "date":data_obj.date,
            "time":data_obj.time,
            "venue":data_obj.venue

        })
    return JsonResponse(data, safe=False)
    # Retrieve the StudentDetails object associated with the Student
