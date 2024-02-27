from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hyd_info(request):
    s = '<h1>Hyderabad jobs information</h1>'
    return HttpResponse(s)

def bng_info(request):
    s = '<h1>Benguluru jobs information</h1>'
    return HttpResponse(s)

def mum_info(request):
    s = '<h1>Mumbhi jobs information</h1>'
    return HttpResponse(s)
