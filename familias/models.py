from django.db import models

from clientes.models import *
from contactos.models import *


class Familia(models.Model):
	nombre = models.CharField(max_length=25)
	cliente = models.ForeignKey(Cliente, related_name="Familia.cliente")
	contactos = models.ManyToManyField(Contacto, db_table="familiacontacto", related_name="Familia.contactos")

	def __unicode__(self):
		return "%s %s" % (self.id, self.nombre)

	class Meta:
		db_table = "familia"
		unique_together = (
			("nombre", "cliente")
		)


