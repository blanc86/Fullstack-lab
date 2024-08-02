from django.shortcuts import render
from django.http import HttpResponse 
from exp9.models import Course, ProjectReg, Student 
# Create your views here.
def course_search_ajax(request): 
    if request.method=="POST": 
        cid=request.POST.get("cname") 
        s=Student.objects.all() 
        student_list=list() 
        for student in s: 
            if student.enrolment.filter(id=cid): 
                student_list.append(student) 
        if len(student_list)==0: 
            return HttpResponse("<h1>No Students enrolled</h1>") 
        return render(request,"selected_students.html",{"student_list":student_list}) 
 
    else: 
        courses=Course.objects.all() 
        return render(request,"course_search_aj.html",{"courses":courses}) 