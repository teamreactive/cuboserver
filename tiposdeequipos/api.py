from clientes.api import ClienteResource
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from .models import TipoDeEquipo


class TipoEquipoResource(ModelResource):
    cliente = fields.ForeignKey(ClienteResource, 'cliente')

    class Meta:
        queryset = TipoDeEquipo.objects.all()
        resource_name = 'tipoequipo'
        authorization = Authorization()