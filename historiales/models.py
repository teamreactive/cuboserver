from django.db import models

from datetime import datetime
from usuarios.models import *


class Historial(models.Model):
	usuario = models.ForeignKey(Usuario, related_name="Historial.usuario", related_name="Historial.usuario")
	fecha = models.DateTimeField(default=datetime.now)
	descripcion = models.TextField()

	def __unicode__(self):
		return "%s %s" % (self.id, self.usuario)

	class Meta:
		db_table = "historial"