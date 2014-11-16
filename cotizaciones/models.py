from django.db import models

from datetime import datetime
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
	iva = models.CharField(max_length=1, choices=IVAS)
	referencia = models.CharField(max_length=25)
	validez = models.CharField(max_length=25)
	formapago = models.CharField(max_length=1, choices=PAGOS)
	proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null = True, related_name="Cotizacion.proveedor")
	fechaentrega = models.DateTimeField()

	def save(self, *args, **kwargs):
		self.id = 1
		try: self.id = Cotizacion.objects.all().order_by("-id")[0].id + 1
		except: pass
		super(Cotizacion, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.id, self.producto)

	class Meta:
		db_table = "cotizacion"
