from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from clientes.api import *
from .models import *


class CentroResource(ModelResource):
	cliente = fields.ForeignKey(ClienteResource, "cliente")
	
	class Meta:
		queryset = Centro.objects.all()
		resource_name = "centro"
		authorization = Authorization()
		filtering = {
			"cliente": ("exact"),
			"nombre": ("exact")
		}