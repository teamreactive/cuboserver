from django.db import models

from clientes.models import Cliente
from contactos.models import Contacto


class FamiliaProveedor(models.Model):
    nombre = models.CharField(max_length=25)
    cliente = models.ForeignKey(Cliente)
    contactos = models.ManyToManyField(Contacto,db_table='familiaproveedorxcontacto')