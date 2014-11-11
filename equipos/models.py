from django.db import models

from clientes.models import *
from tiposequipos.models import *


class Equipo(models.Model):
	nombre = models.CharField(max_length=25)
	descripcion = models.TextField(null=True, blank=True)
	cantidad = models.IntegerField()
	tipoequipo = models.ForeignKey(TipoEquipo, on_delete=models.SET_NULL, null=True, related_name="Equipo.tipoequipo")
	cliente = models.ForeignKey(Cliente, related_name="Equipo.cliente")

	def save(self, *args, **kwargs):
		self.id = Equipo.objects.all().order_by("-id")[0].id + 1
		super(Equipo, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.id, self.nombre)

	class Meta:
		db_table = "equipo"
		unique_together = (
			("nombre", "cliente"),
		)
