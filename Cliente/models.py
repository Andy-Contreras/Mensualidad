from django.db import models
from django.utils import timezone
# Create your models here.
from Trabajo.constantes import Opciones
opc = Opciones()
Genero = opc.genero()


class Clientes(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    genero = models.CharField(max_length=1,choices=Genero, default=Genero[0][0], blank=True, null=True)
    Cedula = models.CharField(max_length=10, blank=False, null=True, unique=True)
    Edad = models.CharField(max_length=2,blank=False)
    email = models.CharField(max_length=100,unique=True)
    fecha_ingreso = models.DateField('Fecha de nacimientos', blank=False, null=False,default=timezone.now)
    
    def __str__(self):
        return "{} ".format(self.nombre)



