import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import appointment
from .forms import CiteForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def sample(request):
    '''Displays a default view'''
    date = datetime.datetime.utcnow()
    return HttpResponse('Vista no asignada\nHora: %s' %date)
#=========================================================================
def homepage(request):
    '''A view dedicate to the main page
    creation where is shown all the options
    that users have.
    :param request: the request call
    :return: the HTML page rendering
    '''
    return render(request, 'homepage.html')
#=========================================================================
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
def Login(request):
    '''A method to let previously registered users
    to login by using their username and password.
    :param request: the request call object
    :return: the rendered login HTML form
    '''
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/newcite')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})
#=========================================================================
def Logout(request):
    '''A standard method to logout
    an user once it has finished its activities
    in the webpage. 
    :param request: the request call object
    :return: gets back the user to homepage
    '''
    logout(request)
    return redirect('/homepage')
#=========================================================================
def show_appointment(request):
    '''An iterative method to show all the listed
    appointments in the DB.
    :param request: the request call object
    :return: the appointments rendered HTML list
    '''
    appoint_dict = {}
    for app in appointment.objects.all():
        appoint_dict[app.name] = app.date
      
    return render(
        request,
        'checklist.html',
        {
            'appoint_dict': appoint_dict,
        }
    )
