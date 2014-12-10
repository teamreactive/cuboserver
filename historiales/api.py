from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from .models import *
from clientes.api import *
from usuarios.api import *


class HistorialResource(ModelResource):
	cliente = fields.ForeignKey(ClienteResource, "cliente", full=True)
	usuario = fields.ForeignKey(UsuarioResource, "usuario", full=True)

	class Meta:
		queryset = Historial.objects.all()
		resource_name = "historial"
		authorization = Authorization()