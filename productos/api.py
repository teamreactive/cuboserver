from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from clientes.api import *
from contactos.api import *
from familias.api import *
from .models import *


class ProductoResource(ModelResource):
	cliente = fields.ForeignKey(ClienteResource, "cliente", null=True)
	familia = fields.ForeignKey(FamiliaResource, "familia")
	#nombres = fields.ToManyField("productos.api.NombreProductoResource", "nombres", related_name="producto", null=True)
	#fotos = fields.ToManyField("productos.api.FotoProductoResource", "fotos", related_name="producto")
	
	class Meta:
		queryset = Producto.objects.all()
		resource_name = "producto"
		authorization = Authorization()
		always_return_data = True

	def obj_create(self, bundle, request=None, **kwargs):
		producto = Producto.objects
		return super(ProductoResource, self).obj_create(bundle)


class NombreProductoResource(ModelResource):
	producto = fields.ToOneField("productos.api.ProductoResource","producto")

	class Meta:
		queryset = NombreProducto.objects.all()
		resource_name = "nombreproducto"
		authorization = Authorization()


class FotoProductoResource(ModelResource):
	producto = fields.ForeignKey(ProductoResource, "producto")

	class Meta:
		queryset = FotoProducto.objects.all()
		resource_name = "fotoproducto"
		authorization = Authorization()


class UnidadProductoResource(ModelResource):
	producto = fields.ForeignKey(ProductoResource, "producto")

	class Meta:
		queryset = UnidadProducto.objects.all()
		resource_name = "unidadproducto"
		authorization = Authorization()


class PrecioMesProductoResource(ModelResource):
	producto = fields.ForeignKey(ProductoResource, "producto")

	class Meta:
		queryset = PrecioMesProducto.objects.all()
		resource_name = "preciomesproducto"
		authorization = Authorization()