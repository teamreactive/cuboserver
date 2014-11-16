from django.db import models

from lugares.models import *
from clientes.models import *
from contactos.models import *


class Proveedor(models.Model):
	razon = models.CharField(max_length=25)
	sigla = models.CharField(max_length=10)
	nit = models.CharField(max_length=25)
	verificacion = models.CharField(max_length=25)
	lugar = models.ForeignKey(Lugar, related_name="Proveedor.lugar")
	logo = models.FileField(upload_to="logos/proovedores")
	cliente = models.ForeignKey(Cliente, related_name="Proveedor.cliente")
	calificacion = models.IntegerField()
	cotizacion = models.BooleanField(default=False)
	contactos = models.ManyToManyField(Contacto, db_table="contactoproveedor", related_name="Proveedor.contactos")

	def save(self, *args, **kwargs):
		self.id = 1
		try: self.id = Proveedor.objects.all().order_by("-id")[0].id + 1
		except: pass
		super(Proveedor, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.id, self.razon)

	class Meta:
		db_table = "proveedor"
		unique_together = (
			("cliente", "nit")
		)