from django.db import models

from datetime import datetime
from usuarios.models import *


class Historial(models.Model):
	usuario = models.ForeignKey(Usuario, related_name="Historial.usuario")
	fecha = models.DateTimeField(default=datetime.now)
	descripcion = models.TextField()

	def save(self, *args, **kwargs):
		self.id = 1
		try: self.id = Historial.objects.all().order_by("-id")[0].id + 1
		except: pass
		super(Historial, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.id, self.usuario)

	class Meta:
		db_table = "historial"