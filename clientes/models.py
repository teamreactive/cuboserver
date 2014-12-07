from django.db import models

from common.upper import UpperCharField

class Cliente(models.Model):
	nit = UpperCharField(max_length=25, unique=True)
	verificacion = UpperCharField(max_length=25, null=True, blank=True, unique=True)
	razon = UpperCharField(max_length=25, unique=True)
	sigla = UpperCharField(max_length=10, null=True, blank=True)
	logo = models.ImageField(upload_to="logos", null=True, blank=True)
	
	def __unicode__(self):
		return "%s %s" % (self.id, self.nit)

	class Meta:
		db_table = "cliente"
