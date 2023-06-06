
from django.db import models


    
class Student(models.Model):
    std_id=models.AutoField(primary_key=True, default=None)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    department = models.CharField(max_length=255)
    courses = models.ManyToManyField('Courses', through='StudentData')


    def __str__(self):
        return self.username
class Courses(models.Model):
    course_id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=100)

    def __str__(self):
        return self.course_name 

class StudentData(models.Model):
    id = models.AutoField(primary_key=True)

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    attendance = models.IntegerField()
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.username} - {self.course.course_name}"
    
class Grades(models.Model):
    id = models.AutoField(primary_key=True)

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    cgpa = models.FloatField()
    gpa1 = models.FloatField()

    gpa2 = models.FloatField()

    gpa3 = models.FloatField()

    gpa4 = models.FloatField()


    def __str__(self):
        return f"{self.student.username} - Grades "

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.username
    
class FEES(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ammount=models.IntegerField()
    status=models.CharField(max_length=10)
    def __str__(self):
        return self.student.username
    
class Examination(models.Model):
    course=models.ForeignKey(Courses, on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    venue=models.CharField(max_length=10)