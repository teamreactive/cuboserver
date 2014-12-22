from django.db import models

from common.upper import UpperCharField


class Cliente(models.Model):
	nit = UpperCharField(max_length=25, unique=True)
	verificacion = UpperCharField(max_length=25, null=True, blank=True, unique=True)
	razon = UpperCharField(max_length=25, unique=True)
	sigla = UpperCharField(max_length=10, null=True, blank=True)
	ciudad = UpperCharField(max_length=50, null=True, blank=True)
	seccion = UpperCharField(max_length=20, null=True, blank=True)
	numero1 = UpperCharField(max_length=5, null=True, blank=True)
	numero2 = UpperCharField(max_length=5, null=True, blank=True)
	numero3 = UpperCharField(max_length=5, null=True, blank=True)
	telefono = UpperCharField(max_length=20, null=True, blank=True)
	sector = UpperCharField(max_length=25, null=True, blank=True)
	logo = models.ImageField(upload_to="logos", null=True, blank=True)
	creador = models.ForeignKey("usuarios.Usuario", related_name="Cliente.creador", null=True)
	
	def __unicode__(self):
		return "%s %s" % (self.id, self.nit)

	class Meta:
		db_table = "cliente"
