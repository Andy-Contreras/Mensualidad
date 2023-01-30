from django.db import models
from django import forms
from django.utils import timezone
from django.forms import ModelForm
from Mensualidad.models import Mensualidad
class CabeceraMensual(ModelForm):
    class Meta:
        model = Mensualidad
        fields = '__all__'
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control '}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(
                         format=('%Y-%m-%d'),
                         attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_finalizacion': forms.DateInput(
                         format=('%Y-%m-%d'),
                         attrs={'class': 'form-control', 'type': 'date'})
        }

