from .models import Student,Courses,StudentData,Grades,Teacher,FEES,Examination
from django.contrib import admin
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'department')
@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name',)
@admin.register(StudentData)
class StudenetDataAdmin(admin.ModelAdmin):
    list_display = ('student','course','attendance','marks')
@admin.register(Grades)
class GradesDataAdmin(admin.ModelAdmin):
    list_display = ('student','cgpa','gpa1','gpa2','gpa3','gpa4')
@admin.register(Teacher)
class GradesDataAdmin(admin.ModelAdmin):
    list_display = ('teacher_id','name','username','password','course')
@admin.register(FEES)
class GradesDataAdmin(admin.ModelAdmin):
    list_display = ('student','ammount','status')
@admin.register(Examination)
class GradesDataAdmin(admin.ModelAdmin):
    list_display = ('course','date','time','venue')