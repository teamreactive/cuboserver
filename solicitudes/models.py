from django.db import models
from django.utils import timezone

from centros.models import *
from common.upper import UpperCharField
from datetime import datetime
from equipos.models import *
from lugares.models import *
from productos.models import *
from usuarios.models import *


class Solicitud(models.Model):
	ESTADOS = (
		("1", "solicitudud de compra creada"),
		("2", "solicitudud de compra rechazada"),
		("3", "solicitudud de compra aprobada"),
		("4", "cotizacion creada")
	)
	estado = UpperCharField(max_length=1, default="1", choices=ESTADOS)
	lugar = models.ForeignKey(Lugar, related_name="Solicitud.lugar")
	fechacreacion = models.DateTimeField(default=timezone.now)
	fecharequerida = models.DateField()
	solicitante = models.ForeignKey(Usuario, related_name="Solicitud.solicitante")
	consolidador = models.ForeignKey(Usuario, related_name="Solicitud.consolidador", null=True)
	aprobador = models.ForeignKey(Usuario, related_name="Solicitud.aprobador", null=True)
	centro = models.ForeignKey(Centro, related_name="Solicitud.centro", null=True)
	equipo = models.ForeignKey(Equipo, related_name="Solicitud.equipo", null=True)
	proyecto = UpperCharField(max_length=25)
	productos = models.ManyToManyField(UnidadProducto, through="ProductoSolicitud", related_name="Solicitud.productos")

	def __unicode__(self):
		return "%s %s" % (self.id, self.solicitante)

	class Meta:
		db_table = "solicitud"

		
class ProductoSolicitud(models.Model):
	linea = models.IntegerField()
	producto = models.ForeignKey(UnidadProducto, related_name="ProductoSolicitud.producto")
	cantidad = models.DecimalField(max_digits=7, decimal_places=2)
	solicitud = models.ForeignKey(Solicitud, related_name="ProductoSolicitud.solicitud")
	estado = UpperCharField(max_length=20, default="")

	def __unicode__(self):
		return "%s %s" % (self.id, self.producto)

	class Meta:
		db_table = "productosolicitud"
		unique_together = (
			"linea", "solicitud"
		)
