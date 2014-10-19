from django.db import models

from contactos.models import Contacto
from usuarios.models import Usuario


class Lugar(models.Model):
    SECCION = (
            ('1','avenida'),
            ('2','calle'),
            ('3','carrera'),
            ('4','diagonal'),
            ('5','transversal'),
        )
    nombre = models.CharField(max_length=100, null=True, blank=True)
    #direccion
    ciudad = models.CharField(max_length=50,null=True,blank=True)
    seccion = models.CharField(max_length=1,null=True,blank=True)
    numero_1 = models.IntegerField(null=True)
    numero_2 = models.IntegerField(null=True)
    numero_3 = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    usuario = models.ForeignKey(Usuario, null=True)
    contactos = models.ManyToManyField(Contacto, db_table='lugaresxcontactos')

    def __unicode__(self):
        return '%s - %s' % (self.nombre)

    class Meta:
        db_table = 'lugar'
        unique_together = (
            ('usuario', 'nombre'),
        )

