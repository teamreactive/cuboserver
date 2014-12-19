from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from clientes.api import *
from .models import *
from tiposequipos.api import *


class EquipoResource(ModelResource):
	cliente = fields.ForeignKey(ClienteResource, "cliente")
	tipo_de_equipo = fields.ForeignKey(TipoEquipoResource, "tipo_de_equipo")

	class Meta:
		queryset = Equipo.objects.all()
		resource_name = "equipo"
		authorization = Authorization()
		filtering = {
			"cliente": ("exact"),
			"nombre": ("exact")
		}