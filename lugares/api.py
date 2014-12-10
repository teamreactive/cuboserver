from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from clientes.api import *
from contactos.api import *
from .models import *


class LugarResource(ModelResource):
	cliente = fields.ForeignKey(ClienteResource, "cliente")

	class Meta:
		queryset = Lugar.objects.all()
		resource_name = "lugar"
		authorization = Authorization()
		filtering = {
			"nombre": ("exact")
		}