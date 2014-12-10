from django.db import models

from clientes.models import *
from common.upper import UpperCharField


class Lugar(models.Model):
	cliente = models.ForeignKey(Cliente, related_name="Lugar.cliente")
	nombre = UpperCharField(max_length=100, null=True)
	ciudad = UpperCharField(max_length=50)
	seccion = UpperCharField(max_length=20)
	numero1 = UpperCharField(max_length=5)
	numero2 = UpperCharField(max_length=5)
	numero3 = UpperCharField(max_length=5)
	telefono = UpperCharField(max_length=20)

	class Meta:
		db_table = "lugar"

