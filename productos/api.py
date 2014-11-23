from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from clientes.api import *
from contactos.api import *
from familias.api import *
from .models import *


class ProductoResource(ModelResource):
	cliente = fields.ForeignKey(ClienteResource, "cliente")
	familia = fields.ForeignKey(FamiliaResource, "familia")

	class Meta:
		queryset = Producto.objects.all()
		resource_name = "producto"
		authorization = Authorization()


class NombreProductoResource(ModelResource):
	producto = fields.ForeignKey(ProductoResource, "producto")

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