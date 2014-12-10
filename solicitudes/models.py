from django.db import models
from django.utils import timezone

from centros.models import *
from common.upper import UpperCharField
from datetime import datetime
from equipos.models import *
from lugares.models import *
from productos.models import *
from usuarios.models import *


class ProductoSolicitud(models.Model):
	linea = models.IntegerField()
	producto = models.ForeignKey(Producto, related_name="ProductoSolicitud.producto")
	unidad = UpperCharField(max_length=20)
	cantidad = models.DecimalField(max_digits=7, decimal_places=2)

	class Meta:
		db_table = "productosolicitud"


class Solicitud(models.Model):
	estado = UpperCharField(max_length=10, default="0100")
	lugar = models.ForeignKey(Lugar, related_name="Solicitud.lugar")
	fechacreacion = models.DateTimeField(default=datetime.now)
	fecharequerida = models.DateField()
	solicitante = models.ForeignKey(Usuario, related_name="Solicitud.solicitante")
	consolidador = models.ForeignKey(Usuario, related_name="Solicitud.consolidador", null=True)
	aprobador = models.ForeignKey(Usuario, related_name="Solicitud.aprobador", null=True)
	centro = models.ForeignKey(Centro, related_name="Solicitud.centro", null=True)
	equipo = models.ForeignKey(Equipo, related_name="Solicitud.equipo", null=True)
	productos = models.ManyToManyField(ProductoSolicitud, related_name="Solicitud.productos")

	class Meta:
		db_table = "solicitud"