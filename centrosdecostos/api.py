from clientes.api import ClienteResource
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource
from .models import CentroDeCosto


class CentroResource(ModelResource):
    cliente = fields.ForeignKey(ClienteResource, 'cliente')
    
    class Meta:
        queryset = CentroDeCosto.objects.all()
        resource_name = 'centro'
        authorization = Authorization()