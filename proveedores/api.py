from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from clientes.api import *
from contactos.api import *
from lugares.api import *
from .models import *


class ProveedorResource(ModelResource):
	cliente = fields.ForeignKey(ClienteResource, "cliente")
	lugar = fields.ForeignKey(LugarResource, "lugar")
	contactos = fields.ToManyFields(ContactoResource, "contactos")

	class Meta:
		queryset = Proveedor.objects.all()
		resource_name = "proveedor"
		authorization = Authorization()