from django.db import models

from clientes.models import Cliente
from contactos.models import Contacto


class FamiliaProveedor(models.Model):
    nombre = models.CharField(max_length=25)
    cliente = models.ForeignKey(Cliente)

    class Meta:
        db_table = 'familia_proveedor'

class ContactosxFamiliaProveedor(models.Model):
    familia_proveedor = models.ForeignKey(FamiliaProveedor)
    contactos = models.ForeignKey(Contacto)

    class Meta:
        db_table = 'contactos_por_familia_proveedor'