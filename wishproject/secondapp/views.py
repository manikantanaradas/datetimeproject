from django.shortcuts import render
from django.http import HttpResponse# Create your views here.
def wish2_info(request):
    return HttpResponse('<h1>Hello this is from second app</h1>')
