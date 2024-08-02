from django.contrib import admin 
 
from exp7.models import Course, Student 
 
# Register your models here. 
#admin.site.register(Student) 
@admin.register(Student) 
class StudentAdmin(admin.ModelAdmin): 
    list_display = ('student_name','student_usn','student_sem') 
    ordering=('student_name',) 
    search_fields = ('student_name',) 
admin.site.register(Course)
