from django.db import models
from django.forms import ModelForm 
from exp7.models import Student , Course
# Create your models here.
class Project(models.Model): 
    student=models.ForeignKey(Student,on_delete=models.CASCADE) 
    ptopic=models.CharField(max_length=200) 
    plangauges=models.CharField(max_length=200) 
    pduration=models.IntegerField() 
 
class ProjectReg(ModelForm): 
    required_css_class="required" 
    class Meta: 
        model=Project 
        fields=['student','ptopic','plangauges','pduration']