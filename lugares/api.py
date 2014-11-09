from contactos.api import ContactoResource
from usuarios.api import UsuarioResource
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from .models import Historial


class LugarResource(ModelResource):
	usuario = fields.ForeignKey(UsuarioResource, 'usuario')
	contactos = field.ToManyField(ContactoResource, 'contactos')

    class Meta:
        queryset = Lugar.objects.all()
        resource_name = 'lugar'
        authorization = Authorization()