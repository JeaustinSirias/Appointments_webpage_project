from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import appointment
from .forms import CiteForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
#=========================================================================
def homepage(request):
    '''A view dedicated to the main page
    creation where is shown all the options
    that users have.

    :param request: the request callout
    :return: the HTML homepage rendering
    '''
    return render(request, 'homepage.html')
#=========================================================================
@login_required
def new_appointment(request):
    '''A view that offers a way to create
    the fillform related to a new appointment asked 
    by an user.

    :param render: the request call
    :return: the rendered appointment HTML form
    '''
    #if request.user.is_authenticated():
    new_form = CiteForm()
    if request.method == 'POST':
        filled_form = CiteForm(request.POST)
        if filled_form.is_valid():
            cite = filled_form.cleaned_data.get('date')
            print(cite)
            for app in appointment.objects.all():
                if cite == app.date:
                    note = 'No hay disponibilidad para la fecha %s' %cite
                    return render(
                        request,
                        'new.html',
                        {
                            'cite_filled':filled_form,
                            'note':note
                        }
                    )    
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
#=========================================================================
def signup(request):
    '''A method to allow register a new user 
    to be able to use the appointment features.

    :param request: the request call
    :return: the sign up rendered HTML form
    '''
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
#=========================================================================
@login_required
def show_appointment(request):
    '''An iterative method to show all the listed
    appointments in the DB.

    :param request: the request call object
    :return: the appointments rendered HTML list
    '''
    appoint_dict = {}
    for app in appointment.objects.all():
        appoint_dict[app.name] = {
            'pk': app.pk,
            'date': app.date,
        }
      
    return render(
        request,
        'checklist.html',
        {
            'appoint_dict': appoint_dict,
        }
    )
#=========================================================================
def modify_appointment(request, id):
    '''A method to update or modify an appointment 
    made by an user.

    :param request: the request call object
    :param id: the primary key of the appointment to modify
    :return: the rendered appointment HTML update form
    '''
    success_note = ''
    appoint = appointment.objects.get(id=id)
    renew_form = CiteForm(instance=appoint)
    if request.method == 'POST':
        form = CiteForm(data=request.POST, instance=appoint)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            for item in appointment.objects.all():
                if date == item.date:
                    none_note = 'No hay disponibilidad para la fecha elegida.'
                    return render(
                        request, 
                        'modify.html', 
                        {
                            'cite_filled': form,
                            'note': none_note,
                        }
                    )
            success_note = 'Se ha actualizado la cita exitosamente'
            form.save()
            renew_form = form

        else:
            invalid_note = 'Solicitud no válida. Vuelva a intentarlo.'
            return render(
                request,
                'modify.html',
                {
                    'cite_filled': form,
                    'note': invalid_note,
                }
                )

    return render(
        request, 
        'modify.html', 
        {
            'cite_filled': renew_form, 
            'note': success_note,
        }
    )
#=========================================================================
def delete_appointment(request, id):
    '''A method for users to delete their
    linked appointents in case they won't 
    need them.

    :param request:
    :param id:
    :return:
    '''
    form = appointment.objects.get(id=id)
    form.delete()
    return redirect(to='show')
#=========================================================================
