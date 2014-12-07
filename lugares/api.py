from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from contactos.api import *
from .models import *
from usuarios.api import *


class LugarResource(ModelResource):
	usuario = fields.ForeignKey(UsuarioResource, "usuario", null=True)
	contactos = fields.ToManyField(ContactoResource, "contactos",)

	class Meta:
		queryset = Lugar.objects.all()
		resource_name = "lugar"
		authorization = Authorization()
		filtering = {
			"nombre": ("exact")
		}