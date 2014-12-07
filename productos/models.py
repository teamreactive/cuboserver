from django.db import models

from centros.models import *
from clientes.models import *
from common.upper import UpperCharField
from contactos.models import *
from equipos.models import *
from familias.models import *


class Producto(models.Model):
	onu = UpperCharField(max_length=25, blank=True, null=True)
	nombre = UpperCharField(max_length=25)
	descripcion = models.TextField()
	referencia = UpperCharField(max_length=25, null=True, blank=True)
	marca = UpperCharField(max_length=25)
	servicio = models.BooleanField(default=False)
	familia = models.ForeignKey(Familia, related_name="Producto.familia", null=True)
	tiempopromedio = models.CharField(max_length=15, null=True, blank=True)
	cliente = models.ForeignKey(Cliente, related_name="productos", null=True)
	valido = models.BooleanField(default=False)
	contactonovende = models.ManyToManyField(Contacto, db_table="productocontactonovende", related_name="Producto.contactonovende")
	contactovende = models.ManyToManyField(Contacto, db_table="productocontactovende", related_name="Producto.contactovende")
	
	def __unicode__(self):
		return "%s %s" % (self.id, self.onu)

	class Meta:
		db_table = "producto"
		unique_together = (
			("cliente", "onu"),
		)


class NombreProducto(models.Model):
	producto = models.ForeignKey(Producto, related_name="nombres")
	nombre = UpperCharField(max_length=25)

	def __unicode__(self):
		return "%s %s" % (self.id, self.producto)

	class Meta:
		db_table = "nombreproducto"
		unique_together = (
			("producto", "nombre")
		)


class FotoProducto(models.Model):
	producto = models.ForeignKey(Producto, related_name="fotos")
	foto = models.ImageField(upload_to="fotoproducto")

	def __unicode__(self):
		return "%s %s" % (self.id, self.producto)

	class Meta:
		db_table = "fotoproducto"


class UnidadProducto(models.Model):
	producto = models.ForeignKey(Producto, related_name="unidades")
	unidad = UpperCharField(max_length=10)
	talla = UpperCharField(max_length=10,null=True,blank=True) # Ask

	def __unicode__(self):
		return "%s %s" % (self.id, self.producto)

	class Meta:
		db_table = "precioproducto"


class PrecioMesProducto(models.Model):
	producto = models.ForeignKey(UnidadProducto, related_name="preciomes")
	mes = UpperCharField(max_length = 2) # 1,2,3,4,5,6,7,8,9,10,11,12
	precio = models.FloatField()

	def __unicode__(self):
		return "%s %s" % (self.id, self.producto)

	class Meta:
		db_table = "preciomesproducto"
