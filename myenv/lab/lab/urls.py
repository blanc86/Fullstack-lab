"""
URL configuration for lab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from exp3.views import current_datetime
from exp4.views import four_hours_ahead,four_hours_ago
from exp5.views import showlist
from exp6.views import home,aboutus,contactus
from exp7.views import reg
from exp9.views import add_project
from exp10.views import StudentDetailView,StudentListView
from exp11.views import construct_csv_from_model,construct_pdf_from_model
from exp12.views import regaj
from exp13.views import course_search_ajax
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cdt/',current_datetime),
    path('fhrsa/',four_hours_ahead),
    path('fhrsh/',four_hours_ago),
    path('showlist/', showlist), 
    path('aboutus/', aboutus), 
    path('home/', home), 
    path('contactus/', contactus),
    path('reg/',reg),
    path('add_project/', add_project),
    path('student_list/', StudentListView.as_view()), 
    path('student_detail/<int:pk>/', StudentDetailView.as_view()),
    path('construct_csv_from_model/', construct_csv_from_model),  
    path('construct_pdf_from_model/', construct_pdf_from_model), 
    path('regaj/',regaj),
    path('course_search_ajax/', course_search_ajax), 
]
