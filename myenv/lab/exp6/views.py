from datetime import date 
from django.http import HttpResponse 
from django.shortcuts import render 
from django.template import Context, Template 
def home(request): 
    return render(request,'home.html') 
def aboutus(request): 
    return render(request,'aboutus.html') 
def contactus(request): 
    return render(request,'contactus.html') 