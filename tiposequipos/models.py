from django.db import models

from clientes.models import Cliente
from common.upper import UpperCharField


class TipoEquipo(models.Model):
	nombre = UpperCharField(max_length=25)
	numero = models.IntegerField(default=0)
	cliente = models.ForeignKey(Cliente, related_name="TipoEquipo.cliente")

	def __unicode__(self):
		return "%s %s" % (self.id, self.nombre)

	class Meta:
		db_table = "tipoequipo"
		unique_together = (
			("cliente", "nombre")
		)