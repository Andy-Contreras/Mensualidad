from django.db import models
from django.utils import timezone
from Cliente.models import Clientes
from django.utils.timezone import now
# Create your models here.



class Mensualidad(models.Model):
    cliente= models.ForeignKey(Clientes, on_delete=models.PROTECT,help_text = "seleccione al cliente ingresado")
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Pago')
    fecha_inicio = models.DateField(default=now)
    fecha_finalizacion= models.DateField(default=now)

    def __str__(self):
        return "{}".format(self.cliente)

    class Meta:
        verbose_name = "Mensualidad"
        verbose_name_plural = "Mensualidades"
        ordering = ('cliente',)