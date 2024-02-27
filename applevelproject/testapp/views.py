from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def exams_view(request):
    return HttpResponse('<h1>Exams View</h1>')

def attendence_view(request):
    return HttpResponse('<h1>Attendence View</h1>')

def fees_view(request):
    return HttpResponse('<h1>Fees View</h1>')
