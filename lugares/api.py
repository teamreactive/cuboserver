from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from common.api import *
from contactos.api import *
from .models import *
from usuarios.api import *


class LugarResource(CORSResource, ModelResource):
	usuario = fields.ForeignKey(UsuarioResource, "usuario")
	contactos = fields.ToManyField(ContactoResource, "contactos")

	class Meta:
		queryset = Lugar.objects.all()
		resource_name = "lugar"
		authorization = Authorization()