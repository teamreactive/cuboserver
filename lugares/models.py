from django.db import models

from contactos.models import Contacto
from usuarios.models import Usuario


class Lugar(models.Model):
    nombre = models.CharField(max_length=25, null=True, blank=True)
    direccion = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    usuario = models.ForeignKey(Usuario, null=True)
    contactos = models.ManyToManyField(Contacto, db_table='lugarxcontactos')

    def __unicode__(self):
        return '%s - %s' % (self.nombre, self.direccion)

    class Meta:
        db_table = 'lugar'
        unique_together = ((usuario,nombre),(usuario,direccion),)

