from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def timeinfo(request):
    date = datetime.datetime.now()
    msg = '<h1>Hello friends good morning</h1>'
    msg = msg+'<h2>Now server time is:'+str(date)+'</h2>'
    return HttpResponse(msg)
