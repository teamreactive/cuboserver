from django.db import models

from lugares.models import Lugar
from clientes.models import Cliente
from contactos.models import Contacto
from proveedores.models import Proveedor


class Proveedor(models.Model):
    COTIZACIONES_DEFECTOS = (
        '0': 'no',
        '1': 'si',
    )
    razon_social = models.CharField(max_length=25)
    sigla = models.CharField(max_length=10)
    nit = models.CharField(max_length=25)
    numero_verificacion = models.CharField(max_length=25)
    lugar = models.ForeignKey(Lugar, related_name='Proveedor.lugar')
    logo = models.FileField(upload_to='logos/proovedores')
    cliente = models.ForeignKey(Cliente, related_name='Proveedor.cliente')
    calificacion = models.IntegerField()
    cotizacion_defecto = models.CharField(choices=COTIZACIONES_DEFECTOS)

class ContactosxProveedor(models.Model):
    contacto = models.ForeignKey(Contacto, related_name='CxP.contacto')
    proveedor = models.ForeignKey(Proveedor, related_name='CxP.proveedor')
