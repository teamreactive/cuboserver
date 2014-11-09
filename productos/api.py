from clientes.api import ClienteResource
from familiasproveedores.api import FamiliaResource
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from .models import *


class ProductoResource(ModelResource):
	cliente = fields.ToManyField(ClienteResource, 'cliente')
	familia_proveedor = fields.ForeignKey(FamiliaResource, 'familia_proveedor')

    class Meta:
        queryset = Producto.objects.all()
        resource_name = 'producto'
        authorization = Authorization()


class NombreProductoResource(ModelResource):
	producto = fields.ForeignKey(ProductoResource, 'producto')

	class Meta:
		queryset = NombresxProducto.objects.all()
		resource_name = 'nombreproducto'
		authorization = Authorization()


class FotoProductoResource(ModelResource):
	producto = fields.ForeignKey(ProductoResource, 'producto')

	class Meta:
		queryset = FotosxProducto.objects.all()
		resource_name = 'fotoproducto'
		authorization = Authorization()


class PrecioProductoResource(ModelResource):
	producto = fields.ForeignKey(ProductoResource, 'producto')

	class Meta:
		queryset = PrecioxProducto.objects.all()
		resource_name = 'precioproducto'
		authorization = Authorization()


class PrecioMesProductoResource(ModelResource):
	producto = fields.ForeignKey(ProductoResource, 'producto')

	class Meta:
		queryset = PrecioProductoXMes.objects.all()
		resource_name = 'preciomesproducto'
		authorization = Authorization()