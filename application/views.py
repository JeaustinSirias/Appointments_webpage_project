import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import appointment
from .forms import CiteForm, SignUpForm
from django.contrib.auth import login, authenticate

def sample(request):
    '''Displays a default view'''
    date = datetime.datetime.utcnow()
    return HttpResponse('Vista no asignada\nHora: %s' %date)

def homepage(request):
    return render(request, 'homepage.html')

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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

