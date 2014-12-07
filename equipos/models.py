from django.db import models

from clientes.models import *
from common.upper import UpperCharField
from tiposequipos.models import *


class Equipo(models.Model):
	nombre = UpperCharField(max_length=25)
	descripcion = models.TextField(null=True, blank=True)
	cantidad = models.IntegerField()
	tipoequipo = models.ForeignKey(TipoEquipo, on_delete=models.SET_NULL, null=True, related_name="Equipo.tipoequipo")
	cliente = models.ForeignKey(Cliente, related_name="Equipo.cliente")

	def __unicode__(self):
		return "%s %s" % (self.id, self.nombre)

	class Meta:
		db_table = "equipo"
		unique_together = (
			("nombre", "cliente"),
		)
