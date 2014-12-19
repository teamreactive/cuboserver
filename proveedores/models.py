from django.db import models

from lugares.models import *
from clientes.models import *
from common.upper import UpperCharField

class Proveedor(models.Model):
	cliente = models.ForeignKey(Cliente, related_name='Proveedor.cliente')
	razon = UpperCharField(max_length=25)
	sigla = UpperCharField(max_length=10)
	nit = UpperCharField(max_length=25)
	verificacion = UpperCharField(max_length=25)
	ciudad = UpperCharField(max_length=50)
	seccion = UpperCharField(max_length=20)
	numero1 = UpperCharField(max_length=5)
	numero2 = UpperCharField(max_length=5)
	numero3 = UpperCharField(max_length=5)
	telefono = UpperCharField(max_length=20)
	logo = models.ImageField(upload_to="logos/proovedores")

	class Meta:
		db_table = "proveedor"