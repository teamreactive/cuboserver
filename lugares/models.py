from django.db import models

from contactos.models import Contacto
from clientes.models import Cliente

class Lugar(models.Model):
    SECCIONES = (
        ('1', 'calle'),
        ('2', 'carrera'),
        ('3', 'transversal'),
        ('4', 'avenida'),
        ('5', 'diagonal'),
    )
    nombre = models.CharField(max_length=25, null=True)
    seccion = models.CharField(max_length=1, choices=SECCIONES)
    numero_seccion = models.CharField(max_length=5)
    numero_1 = models.CharField(max_length=5)
    numero_2 = models.CharField(max_length=5)
    client = models.ForeignKey(Cliente)
#
class LugarxContacto(models.Model):
    lugar = models.ForeignKey(Lugar, related_name='LxC.lugar')
    contacto = models.ForeignKey(Contacto, related_name='LxC.contacto')