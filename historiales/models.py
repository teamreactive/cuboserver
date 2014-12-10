from django.db import models

from clientes.models import *
from common.upper import UpperCharField
from datetime import datetime
from usuarios.models import *


class Historial(models.Model):
	cliente = models.ForeignKey(Cliente, related_name="Historial.cliente")
	usuario = models.ForeignKey(Usuario, related_name="Historial.usuario")
	fecha = models.DateTimeField(default=datetime.now)
	descripcion = models.TextField()

	def __unicode__(self):
		return "%s %s" % (self.id, self.usuario)

	class Meta:
		db_table = "historial"