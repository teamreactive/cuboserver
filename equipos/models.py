from django.db import models

from clientes.models import Cliente
from tiposdeequipos.models import TipoDeEquipo


class Equipo(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField(null=True, blank=True)
    cantidad = models.IntegerField()
    tipo_de_equipo = models.ForeignKey(TipoDeEquipo, on_delete=models.SET_NULL)
    cliente = models.ForeignKey(Cliente)
