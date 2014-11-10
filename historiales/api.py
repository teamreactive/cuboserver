from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from .models import *
from usuarios.api import *


class HistorialResource(ModelResource):
	usuario = fields.ForeignKey(UsuarioResource, "usuario")

	class Meta:
		queryset = Historial.objects.all()
		resource_name = "historial"
		authorization = Authorization()