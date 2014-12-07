from django.db import models

from datetime import datetime
from common.upper import UpperCharField
from proveedores.models import *
from solicitudes.models import *


class Cotizacion(models.Model):
	IVAS = (
		("1", "16"),
		("2", "1.6"), 
		("3", "20"),
		("4", "0")
	)

	PAGOS = (
		("1", "anticipado"),
		("2", "contado"),
		("3", "dias")
	)

	producto = models.ForeignKey(ProductoSolicitud, on_delete=models.PROTECT, related_name="Cotizacion.producto")
	preciounitario = models.DecimalField(max_digits=12,decimal_places=2)
	iva = UpperCharField(max_length=1, choices=IVAS)
	referencia = UpperCharField(max_length=25)
	validez = UpperCharField(max_length=25)
	formapago = UpperCharField(max_length=1, choices=PAGOS)
	proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null = True, related_name="Cotizacion.proveedor")
	fechaentrega = models.DateTimeField()

	def __unicode__(self):
		return "%s %s" % (self.id, self.producto)

	class Meta:
		db_table = "cotizacion"
