from django.db import models

from clientes.models import Cliente


class TipoDeEquipo(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField(null=True)
    cliente = models.ForeignKey(Cliente)