from django import forms
from .models import appointment


class citeForm(forms.ModelForm):

    class Meta:
        model = appointment
        fields = [
            'name',
            'date',
        ]

        labels = {
            'name' = 'Nombre',
            'date' = 'Fecha',
        }
