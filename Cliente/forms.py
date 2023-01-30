from django import forms
from django.utils import timezone
from django.forms import ModelForm
from Cliente.models import Clientes

class ClienteForms(ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'
        widgets = {
            'cedula': forms.NumberInput(attrs={'class': 'form-control','placerholder': 'Ingrese su número de cédula'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control','placerholder': 'Ingrese la edad'}),
            'fecha_ingreso': forms.DateInput(
                         format=('%Y-%m-%d'),
                         attrs={'class': 'form-control', 'type': 'date'}
          ),
        }