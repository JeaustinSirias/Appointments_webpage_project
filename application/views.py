import datetime
from django.http import HttpResponse
from django.shortcuts import render

from .models import appointment
from .forms import CiteForm

def sample(request):
    '''Displays a default view'''
    date = datetime.datetime.utcnow()
    return HttpResponse('Vista no asignada\nHora: %s' %date)

def new_appointment(request):
    new_form = CiteForm()
    if request.method == 'POST':
        filled_form = CiteForm(request.POST)

        if filled_form.is_valid():
            new_cite = filled_form.save()
            note = (
                'Cita a nombre de: \'{}\' fue creada para la fecha \'{}\' \n'.format(
                    new_cite.name, new_cite.date
                )
            )
        else:
            note = 'Solicitud no válida. Vuelva a intentarlo.'

        return render(
            request,
            'new.html',
            {
                'cite_filled': filled_form,
                'note': note,
            }
            )
    else:
        return render(
            request,
            'new.html',
            {
                'cite_filled': new_form,
            }
        )

def delete_appointment(request):
    return

def check_appointment(request):
    return
