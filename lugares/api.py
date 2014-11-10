from contactos.api import ContactoResource
from usuarios.api import UsuarioResource
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource
from .models import Lugar


class LugarResource(ModelResource):
    usuario = fields.ForeignKey(UsuarioResource, 'usuario')
    contactos = fields.ToManyField(ContactoResource, 'contactos')

    class Meta:
        queryset = Lugar.objects.all()
        resource_name = 'lugar'
        authorization = Authorization()