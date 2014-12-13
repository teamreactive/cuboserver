from django.db import models

from datetime import datetime
from common.upper import UpperCharField
from proveedores.models import *
from solicitudes.models import *
from productos.models import *


class Cotizacion(models.Model):
	producto = models.ForeignKey(Producto, related_name="Cotizacion.producto")
	preciounitario = models.DecimalField(max_digits=12, decimal_places=2)
	iva = models.DecimalField(max_digits=6, decimal_places=3)
	tiempo = models.IntegerField()
	referencia = UpperCharField(max_length=25)
	validez = models.IntegerField()
	formapago = UpperCharField(max_length=20)
	proveedor = models.ForeignKey(Proveedor, related_name="Cotizacion.proveedor", null=True)

	def __unicode__(self):
		return "%s %s" % (self.id, self.producto)

	class Meta:
		db_table = "cotizacion"
