from django.db import models

from cotizaciones.models import *
from datetime import datetime


class Compra(models.Model):
	cotizacion = models.ForeignKey(Cotizacion, related_name="Compra.cotizacion")
	fechaentregado = models.DateTimeField(default=datetime.now)
	entregaparcial = models.DateTimeField(default=datetime.now)
	porcentajedevolucion = models.DecimalField(max_digits=5, decimal_places=2)

	def save(self, *args, **kwargs):
		self.id = Compra.objects.all().order_by("-id")[0].id + 1
		super(Compra, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.id, self.cotizacion)

	class Meta:
		db_table = "compra"
