from django.db import models

from clientes.models import Cliente


class TipoEquipo(models.Model):
	nombre = models.CharField(max_length=25)
	descripcion = models.TextField(null=True, blank=True)
	cliente = models.ForeignKey(Cliente, related_name="TipoEquipo.cliente")

	def save(self, *args, **kwargs):
		self.id = TipoEquipo.objects.all().order_by("-id")[0].id + 1
		super(TipoEquipo, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.id, self.nombre)

	class Meta:
		db_table = "tipoequipo"
		unique_together = (
			("cliente", "nombre")
		)