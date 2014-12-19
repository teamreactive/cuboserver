from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from clientes.api import *
from .models import *


class FamiliaResource(ModelResource):
	cliente = fields.ForeignKey(ClienteResource, "cliente")

	class Meta:
		queryset = Familia.objects.all()
		resource_name = "familia"
		authorization = Authorization()
		filtering = {
			"nombre": ("exact"),
			"cliente": ("exact")
		}