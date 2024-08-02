from django.http import HttpResponse 
from django.shortcuts import render 
from django.template import Context, Template 
# Create your views here. 
def showlist(request): 
    fruits=["Mango","Apple","Bananan","Jackfruits"] 
    student_names=["Tony","Mony","Sony","Bob"] 
    return render(request,'showlist.html',{"fruits":fruits,"student_names":student_names}
 )