from django.db import models

from centros.models import *
from clientes.models import *
from contactos.models import *
from equipos.models import *
from familias.models import *


class Producto(models.Model):
	onu = models.CharField(max_length=25, blank=True, null=True)
	nombre = models.CharField(max_length=25)
	descripcion = models.TextField(null=True,blank=True)
	referencia = models.CharField(max_length=25, null=True,blank=True)
	marca = models.CharField(max_length=25)
	servicio = models.BooleanField(default=False)
	familia = models.ForeignKey(Familia, null=True, related_name="Producto.familia")
	tiempopromedio = models.CharField(max_length=15, null=True, blank=True)
	cliente = models.ForeignKey(Cliente, related_name="Producto.cliente")
	valido = models.BooleanField(default=False)
	contactonovende = models.ManyToManyField(Contacto, db_table="productocontactonovende", related_name="Producto.contactonovende")
	contactovende = models.ManyToManyField(Contacto, db_table="productocontactovende", related_name="Producto.contactovende")

	def save(self, *args, **kwargs):
		self.id = Producto.objects.all().order_by("-id")[0].id + 1
		super(Producto, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return "%s %s" % (self.id, self.onu)

	class Meta:
		db_table = "producto"
		unique_together = (
			("cliente", "onu"),
		)


class NombreProducto(models.Model):
	producto = models.ForeignKey(Producto, related_name="NombreProducto.producto")
	nombre = models.CharField(max_length=25)

	def save(self, *args, **kwargs):
		self.id = NombreProducto.objects.all().order_by("-id")[0].id + 1
		super(NombreProducto, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.id, self.producto)

	class Meta:
		db_table = "nombreproducto"
		unique_together = (
			("producto", "nombre")
		)


class FotoProducto(models.Model):
	producto = models.ForeignKey(Producto, related_name="FotoProducto.producto")
	foto = models.ImageField(upload_to="fotoproducto")

	def save(self, *args, **kwargs):
		self.id = FotoProducto.objects.all().order_by("-id")[0].id + 1
		super(FotoProducto, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.id, self.producto)

	class Meta:
		db_table = "fotoproducto"


class UnidadProducto(models.Model):
	producto = models.ForeignKey(Producto, related_name="UnidadProducto.producto")
	unidad = models.CharField(max_length=10)
	talla = models.CharField(max_length=10,null=True,blank=True) # Ask

	def save(self, *args, **kwargs):
		self.id = UnidadProducto.objects.all().order_by("-id")[0].id + 1
		super(UnidadProducto, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.id, self.producto)

	class Meta:
		db_table = "precioproducto"


class PrecioMesProducto(models.Model):
	producto = models.ForeignKey(UnidadProducto, related_name="PrecioMesProducto.producto")
	mes = models.CharField(max_length = 2) # 1,2,3,4,5,6,7,8,9,10,11,12
	precio = models.FloatField()

	def save(self, *args, **kwargs):
		self.id = PrecioMesProducto.objects.all().order_by("-id")[0].id + 1
		super(PrecioMesProducto, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.id, self.producto)

	class Meta:
		db_table = "preciomesproducto"
