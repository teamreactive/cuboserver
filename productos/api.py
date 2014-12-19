from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS

from clientes.api import *
from contactos.api import *
from familias.api import *
from .models import *


class NombreProductoResource(ModelResource):
	cliente = fields.ForeignKey(ClienteResource, "cliente")
	
	class Meta:
		queryset = NombreProducto.objects.all()
		resource_name = "nombreproducto"
		authorization = Authorization()
		filtering = {
			"cliente": ("exact"),
			"nombre": ("exact")
		}


class UnidadProductoResource(ModelResource):
	
	class Meta:
		queryset = UnidadProducto.objects.all()
		resource_name = "unidadproducto"
		authorization = Authorization()
		filtering = {
			"unidad": ("exact")
		}


class ProductoResource(ModelResource):
	cliente = fields.ForeignKey(ClienteResource, "cliente")
	familia = fields.ForeignKey(FamiliaResource, "familia", null=True)
	nombres = fields.ToManyField(NombreProductoResource, "nombres", full=True)
	unidades = fields.ToManyField(UnidadProductoResource, "unidades", full=True)
	foto = fields.FileField(attribute="img", null=True, blank=True)
		
	class Meta:
		queryset = Producto.objects.all()
		resource_name = "producto"
		authorization = Authorization()
		always_return_data = True
		filtering = {
			"cliente": ("exact"),
			"activo": ("exact")
		}