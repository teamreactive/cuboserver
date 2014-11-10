from django.db import models

from clientes.models import *


class Centro(models.Model):
	nombre = models.CharField(max_length=25)
	cliente = models.ForeignKey(Cliente, related_name="Centro.cliente")

	def __unicode__(self):
		return "%s %s" % (self.id, self.nombre)

	class Meta:
		db_table = "centro"
		unique_together = (
			("nombre", "cliente")
		)