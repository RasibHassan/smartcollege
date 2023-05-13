
from django.db import models
from jsonfield import JSONField

class Student(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    department = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class StudentDetails(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='courses')

    courses = JSONField(default=list)
    attendance =JSONField(default=dict)
    mid_marks = JSONField(default=dict)

    def __str__(self):
        return f"{self.student.username}'s Details"
