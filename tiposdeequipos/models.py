from django.db import models

from clientes.models import Cliente


class TipoDeEquipo(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente)

    class Meta:
        db_table = 'tipo_de_equipo'