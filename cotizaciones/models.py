from django.db import models

from datetime import datetime
from productos.models import Product
from proveedores.models import Proveedor


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
    producto = models.ForeignKey(Product)
    precio_unitario = models.CharField(max_length=10)
    iva = models.CharField(max_length=1, choices=IVAS)
    tiempo_entrega = models.CharField(max_length=10)
    referencia = models.CharField(max_length=25)
    validez = models.CharField(max_length=25)
    forma_de_pago = models.CharField(max_length=1, choices=PAGOS)
    proveedor = models.ForeignKey(Proveedor)
    fecha_entrega = models.DateTimeField(default=datetime.now)