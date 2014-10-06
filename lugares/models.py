from django.db import models

from contactos.models import Contacto
from usuarios.models import Usuario


class Lugar(models.Model):
    nombre = models.CharField(max_length=25, null=True, blank=True)
    direccion = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, null=True)
    contactos = models.ManyToManyField(Contacto, db_table='lugarxcontactos')

    class Meta:
        db_table = 'lugar'

