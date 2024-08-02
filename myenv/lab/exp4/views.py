from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import datetime
def four_hours_ahead(request):
    dt = datetime.datetime.now() + datetime.timedelta(hours=4)
    html = "<html><body><h1>Date and Time four hours ahead:%s</h1></body></html>"%dt
    return HttpResponse(html)

def four_hours_ago(request):
    dt = datetime.datetime.now() + datetime.timedelta(hours=-4)
    html = "<html><body><h1>Date and Time four hours ago:%s</h1></body></html>"%dt
    return HttpResponse(html)