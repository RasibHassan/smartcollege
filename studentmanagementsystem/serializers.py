from rest_framework import serializers
from .models import Student,StudentData
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['std_id','username', 'password', 'department']

class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        fields = ['course','attendance','marks']
class GradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        fields = ['cgpa','gpa1','gpa2','gpa3','gpa4']