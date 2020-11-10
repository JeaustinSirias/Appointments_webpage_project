from django import forms
from .models import appointment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CiteForm(forms.ModelForm):
    '''The form for the appointment 
    model'''
    #fecha = forms.DateField(help_text='Formato dd/mm/aaaa')

    class Meta:
        model = appointment
        fields = [
            'name',
            'date',
        ]

        labels = {
            'name': 'Nombre',
            'date': 'Fecha',
        }

class SignUpForm(UserCreationForm):
    '''The form model for the standard Django 
    User model, but with first_name and email
    entries custom'''
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2', )