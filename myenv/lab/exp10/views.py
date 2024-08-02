from django.shortcuts import render
from exp7.models import Student,Course

from django.views import generic 
class StudentListView(generic.ListView): 
    model=Student 
    template_name="student_list.html" 
 
class StudentDetailView(generic.DetailView): 
    model=Student 
    template_name="student_detail.html"