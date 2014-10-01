from django.db import models

from clientes.models import Cliente


class CentroDeCosto(models.Model):
    nombre = models.CharField(max_length=25)
    cliente = models.ForeignKey(Cliente)