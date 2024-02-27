from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish3_info(request):
    return HttpResponse('<h1>Thsi is from third app</h1>')
