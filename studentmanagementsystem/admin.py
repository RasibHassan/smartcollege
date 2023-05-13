from .models import Student, StudentDetails
from django.contrib import admin
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'department')

@admin.register(StudentDetails)
class StudentDetailsAdmin(admin.ModelAdmin):
    list_display = ('student', 'get_courses', 'get_attendance', 'get_mid_marks')

    def get_courses(self, obj):
        return ", ".join(obj.courses)

    def get_attendance(self, obj):
        return "\n".join([f"{course}: {attendance[0]}/{attendance[1]}" for course, attendance in obj.attendance.items()])

    def get_mid_marks(self, obj):
        return "\n".join([f"{course}: {marks}" for course, marks in obj.mid_marks.items()])

    get_courses.short_description = 'Courses'
    get_attendance.short_description = 'Attendance'
    get_mid_marks.short_description = 'Mid-Marks'
# Register your models here.
