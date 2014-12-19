from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from .models import *


class ProveedorResource(ModelResource):
	cliente = fields.ForeignKey("clientes.api.ClienteResource", "cliente")

	class Meta:
		queryset = Proveedor.objects.all()
		resource_name = "proveedor"
		authorization = Authorization()
		filtering = {
			"razon": ("exact"),
			"cliente": ("exact")
		}