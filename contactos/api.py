from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from .models import *


class ContactoResource(ModelResource):
	cliente = fields.ForeignKey("clientes.api.ClienteResource", "cliente")
	proveedor = fields.ForeignKey("proveedores.api.ProveedorResource", "proveedor", null=True)
	familia = fields.ForeignKey("familias.api.FamiliaResource", "familia", null=True)

	class Meta:
		queryset = Contacto.objects.all()
		resource_name = "contacto"
		authorization = Authorization()
		filtering = {
			"cliente": ("exact")
		}