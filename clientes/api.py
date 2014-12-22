from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from .models import *


class ClienteResource(ModelResource):
	creador = fields.ForeignKey("usuarios.api.UsuarioResource", "creador", null=True)

	class Meta:
		queryset = Cliente.objects.all()
		resource_name = "cliente"
		authorization = Authorization()
		always_return_data = True
		filtering = {
			"nit": ("exact"),
			"razon": ("exact")
		}