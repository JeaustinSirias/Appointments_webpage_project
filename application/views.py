import datetime
from django.http import HttpResponse
from django 

def sample(request):
    '''Displays a default view'''
    date = datetime.datetime.utcnow()
    return HttpResponse('Vista no asignada\nHora: %s' %date)

def new_appointment(request):
    return

def delete_appointment(request):
    return

def check_appointment(request):
    return



