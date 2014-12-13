from django.db import models

from cotizaciones.models import *
from datetime import datetime


class Compra(models.Model):
	cotizacion = models.ForeignKey(Cotizacion, related_name="Compra.cotizacion", null=True)
	fechaentregado = models.DateTimeField(default=datetime.now)
	entregaparcial = models.DateTimeField(default=datetime.now)
	porcentajedevolucion = models.DecimalField(max_digits=5, decimal_places=2)

	def __unicode__(self):
		return "%s %s" % (self.id, self.cotizacion)

	class Meta:
		db_table = "compra"
