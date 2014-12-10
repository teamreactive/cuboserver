from django.db import models

from lugares.models import *
from clientes.models import *
from common.upper import UpperCharField
from contactos.models import *

class Proveedor(models.Model):
	razon = UpperCharField(max_length=25)
	sigla = UpperCharField(max_length=10)
	nit = UpperCharField(max_length=25)
	verificacion = UpperCharField(max_length=25)
	lugar = models.ForeignKey(Lugar, related_name="Proveedor.lugar")
	logo = models.FileField(upload_to="logos/proovedores")

	class Meta:
		db_table = "proveedor"