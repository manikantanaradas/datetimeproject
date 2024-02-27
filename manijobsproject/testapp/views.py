from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hydjobsinfo(request):
    s='<h1>Hyderbad Jobs Information</h1>'
    return HttpResponse(s)

def bngjobsinfo(request):
    s='<h1>Benguluru Jobs Information</h1>'
    return HttpResponse(s)

def punejobsinfo(request):
    s='<h1>Pune Jobs Information</h1>'
    return HttpResponse(s)
