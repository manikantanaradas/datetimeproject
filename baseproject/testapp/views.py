from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_view(request):
    return HttpResponse('<h1>First View Response</h1>')

def second_view(request):
    return HttpResponse('<h1>second View Response</h1>')

def third_view(request):
    return HttpResponse('<h1>third View Response</h1>')

def fourth_view(request):
    return HttpResponse('<h1>fourth View Response</h1>')

def fifth_view(request):
    return HttpResponse('<h1>fifth View Response</h1>')
