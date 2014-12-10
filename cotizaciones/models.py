from django.db import models

from datetime import datetime
from common.upper import UpperCharField
from proveedores.models import *
from solicitudes.models import *


class Cotizacion(models.Model):
	producto = models.ForeignKey(ProductoSolicitud, on_delete=models.PROTECT, related_name="Cotizacion.producto")
	preciounitario = models.DecimalField(max_digits=12, decimal_places=2)
	ivaa = models.DecimalField(max_digits=6, decimal_places=3)
	tiempo = models.IntegerField()
	referencia = UpperCharField(max_length=25)
	validez = UpperCharField(max_length=25)
	formapago = UpperCharField(max_length=10)
	proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null = True, related_name="Cotizacion.proveedor")

	def __unicode__(self):
		return "%s %s" % (self.id, self.producto)

	class Meta:
		db_table = "cotizacion"
