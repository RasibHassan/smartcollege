from rest_framework import serializers
from .models import Student, StudentDetails

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['username', 'password', 'department']

class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = ['courses', 'attendance', 'mid_marks']