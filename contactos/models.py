from django.db import models

from common.upper import UpperCharField

class Contacto(models.Model):
	nombre = UpperCharField(max_length=25)
	apellido = UpperCharField(max_length=25)
	telefono = UpperCharField(max_length=15, null=True, blank=True)
	extension = UpperCharField(max_length=5, null=True, blank=True)
	celular = UpperCharField(max_length=15, null=True, blank=True)
	email = UpperCharField(max_length=320, null=True, blank=True)
	cargo = UpperCharField(max_length=25, null=True, blank=True)
	perfil = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return "%s %s" % (self.id, self.nombre)

	class Meta:
		db_table = "contacto"
