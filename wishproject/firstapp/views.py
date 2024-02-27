from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish1_info(request):
    return HttpResponse('<h1>hello This is from firstapp</h1>')
