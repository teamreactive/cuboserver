from usuarios.api import UsuarioResource
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from .models import Historial


class HistorialResource(ModelResource):
	usuario = fields.ForeignKey(UsuarioResource, 'usuario')

    class Meta:
        queryset = Historial.objects.all()
        resource_name = 'historial'
        authorization = Authorization()