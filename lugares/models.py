from django.db import models

from contactos.models import *
from usuarios.models import *


class Lugar(models.Model):
	SECCION = (
		("1","avenida"),
		("2","calle"),
		("3","carrera"),
		("4","diagonal"),
		("5","transversal")
	)

	nombre = models.CharField(max_length=100, null=True, blank=True)
	ciudad = models.CharField(max_length=50,null=True,blank=True)
	seccion = models.CharField(max_length=1,null=True,blank=True)
	numero1 = models.IntegerField(null=True)
	numero2 = models.IntegerField(null=True)
	numero3 = models.IntegerField(null=True)
	descripcion = models.CharField(max_length=200, null=True, blank=True)
	usuario = models.ForeignKey(Usuario, null=True, related_name="Lugar.usuario")
	contactos = models.ManyToManyField(Contacto, db_table="lugarcontacto")

	def save(self, *args, **kwargs):
		self.id = 1
		try: self.id = Lugar.objects.all().order_by("-id")[0].id + 1
		except: pass
		super(Lugar, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.id, self.nombre)

	class Meta:
		db_table = "lugar"
		unique_together = (
			("usuario", "nombre")
		)

