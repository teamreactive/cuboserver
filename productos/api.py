from clientes.api import ClienteResource
from contactos.api import ContactoResource
from familiasproveedores.api import FamiliaResource
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from .models import *


class ProductoResource(ModelResource):
	cliente = fields.ToManyField(ClienteResource, 'cliente')
	familia_proveedor = fields.ForeignKey(FamiliaResource, 'familia_proveedor')
	contacto_novende = fields.ToManyField(ContactoResource, 'contacto_novende')
	contacto_vende = fields.ToManyField(ContactoResource, 'contacto_vende')

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


class UnidadProductoResource(ModelResource):
	producto = fields.ForeignKey(ProductoResource, 'producto')

	class Meta:
		queryset = UnidadXProducto.objects.all()
		resource_name = 'unidadproducto'
		authorization = Authorization()


class PrecioMesProductoResource(ModelResource):
	producto = fields.ForeignKey(ProductoResource, 'producto')

	class Meta:
		queryset = PrecioProductoXMes.objects.all()
		resource_name = 'preciomesproducto'
		authorization = Authorization()