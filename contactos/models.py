from django.db import models

from common.upper import UpperCharField
from clientes.models import *
from familias.models import *
from proveedores.models import *


class Contacto(models.Model):
	cliente = models.ForeignKey(Cliente, related_name="Contacto.cliente")
	proveedor = models.ForeignKey(Proveedor, related_name="Contacto.proveedor", null=True)
	nombre = UpperCharField(max_length=50)
	apellido = UpperCharField(max_length=50)
	telefono = UpperCharField(max_length=15, null=True, blank=True)
	extension = UpperCharField(max_length=5, null=True, blank=True)
	celular = UpperCharField(max_length=15, null=True, blank=True)
	email = UpperCharField(max_length=320, null=True, blank=True)
	cargo = UpperCharField(max_length=25, null=True, blank=True)
	perfil = models.TextField(null=True, blank=True)
	familia = models.ForeignKey(Familia, related_name="Contacto.familia", null=True)

	def __unicode__(self):
		return "%s %s" % (self.id, self.nombre)

	class Meta:
		db_table = "contacto"
