from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from clientes.api import *
from .models import *


class TipoEquipoResource(ModelResource):
	cliente = fields.ForeignKey(ClienteResource, "cliente")

	class Meta:
		queryset = TipoEquipo.objects.all()
		resource_name = "tipoequipo"
		authorization = Authorization()
		filtering = {
			"nombre": ("exact"),
			"cliente": ("exact")
		}