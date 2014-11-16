from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from clientes.api import *
from contactos.api import *
from .models import *


class FamiliaResource(ModelResource):
	cliente = fields.ForeignKey(ClienteResource, "cliente")
	contactos = fields.ToManyField(ContactoResource, "contactos")

	class Meta:
		queryset = Familia.objects.all()
		resource_name = "familia"
		authorization = Authorization()