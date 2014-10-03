from django.db import models

from clientes.models import Cliente
from tiposdeequipos.models import TipoDeEquipo


class Equipo(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField(null=True)
    cantidad = models.IntegerField(max_length=10)
    tipo_de_equipo = models.ForeignKey(TipoDeEquipo)
    cliente = models.ForeignKey(Cliente)
