from django.db import models

from lugares.models import Lugar
from clientes.models import Cliente
from contactos.models import Contacto


class Proveedor(models.Model):
    razon_social = models.CharField(max_length=25)
    sigla = models.CharField(max_length=10)
    nit = models.CharField(max_length=25)
    numero_verificacion = models.CharField(max_length=25)
    lugar = models.ForeignKey(Lugar, related_name='Proveedor.lugar')
    logo = models.FileField(upload_to='logos/proovedores')
    cliente = models.ForeignKey(Cliente, related_name='Proveedor.cliente')
    calificacion = models.IntegerField()
    cotizacion_defecto = models.BooleanField(default=False)

    class Meta:
        db_table = 'proveedor'
        unique_together = ((cliente,nit))

class ContactosxProveedor(models.Model):
    contacto = models.ForeignKey(Contacto, related_name='CxP.contacto')
    proveedor = models.ForeignKey(Proveedor, related_name='CxP.proveedor')

    class Meta:
        db_table = 'contacto_por_proveedor'
