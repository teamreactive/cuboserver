from django.db import models

from centros.models import *
from clientes.models import *
from common.upper import UpperCharField
from contactos.models import *
from equipos.models import *
from familias.models import *


class NombreProducto(models.Model):
	cliente = models.ForeignKey(Cliente, related_name="NombreProducto.cliente")
	nombre = UpperCharField(max_length=100)

	class Meta:
		db_table = "nombreproducto"


class UnidadProducto(models.Model):
	unidad = UpperCharField(max_length=10)

	class Meta:
		db_table = "unidadproducto"


class Producto(models.Model):
	cliente = models.ForeignKey(Cliente, related_name="Producto.cliente")
	activo = models.BooleanField(default=False)
	nombres = models.ManyToManyField(NombreProducto, related_name="Producto.nombres")
	onu = UpperCharField(max_length=50, blank=True, null=True)
	tipo = UpperCharField(max_length=10)
	descripcion = models.TextField()
	referencia = UpperCharField(max_length=50, null=True, blank=True)
	talla = UpperCharField(max_length=25, null=True, blank=True)
	marca = UpperCharField(max_length=50)
	unidades = models.ManyToManyField(UnidadProducto, related_name="Producto.unidades")
	familia = models.ForeignKey(Familia, related_name="Producto.familia", null=True)
	foto = models.ImageField(upload_to="fotosproductos", null=True)

	class Meta:
		db_table = "producto"