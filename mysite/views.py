'''
Created on 23/7/2014

@author: ASUS
'''
#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_time.html', locals())

def hours_ahead(request, offset):
    offset = int(offset)
    dt =datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.<body><html>" %(offset, dt)
    return HttpResponse(html)

    
