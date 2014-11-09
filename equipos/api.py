from clientes.api import ClienteResource
from tiposdeequipos.api import TipoEquipoResource
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from .models import Equipo


class EquipoResource(ModelResource):
	cliente = fields.ForeignKey(ClienteResource, 'cliente')
	tipo_de_equipo = fields.ForeignKey(TipoEquipoResource, 'tipo_de_equipo')

    class Meta:
        queryset = Equipo.objects.all()
        resource_name = 'equipo'
        authorization = Authorization()