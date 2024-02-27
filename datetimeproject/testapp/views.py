from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def datetimeinfo(request):
    date=datetime.datetime.now()
    h=int(date.strftime("%H"))
    msg='<h1>Hello Guest'
    if h<12:
        msg += 'GoodMorning'
    elif h<16:
        msg += "Good Afternoon"
    elif h<21:
        msg += "Good Evening"
    else:
        msg += "GoodNight"
    msg += '</h1><hr>'
    msg += '<h1>Now the server time is:'+str(date)+'</h1>'
    return HttpResponse(msg)
