from django.db import models

from datetime import datetime
from proveedores.models import Proveedor
from solicitudes.models import ProductoXSolicitud


class Cotizacion(models.Model):
    IVAS = (
        ('1', '16'),
        ('2', '1.6'), 
        ('3', '20'),
        ('4', '0'),
    )
    PAGOS = (
        ('1', 'anticipado'),
        ('2', 'contado'),
        ('3', 'dias'),
    )
    producto = models.ForeignKey(ProductoXSolicitud, on_delete=models.PROTECT)
    precio_unitario = models.DecimalField(max_digits=12,decimal_places=2)
    iva = models.CharField(max_length=1, choices=IVAS)
    referencia = models.CharField(max_length=25)
    validez = models.CharField(max_length=25)
    forma_de_pago = models.CharField(max_length=1, choices=PAGOS)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null = True)
    fecha_entrega = models.DateTimeField()

    class Meta:
        db_table = 'cotizacion'
