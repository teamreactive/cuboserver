from clientes.api import ClienteResource
from contactos.api import ContactoResource
from lugares.api import LugarResource
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource
from .models import *


class ProveedorResource(ModelResource):
    cliente = fields.ForeignKey(ClienteResource, 'cliente')
    lugar = fields.ForeignKey(LugarResource, 'lugar')

    class Meta:
        queryset = Proveedor.objects.all()
        resource_name = 'proveedor'
        authorization = Authorization()


class ContactoProveedorResource(ModelResource):
    contacto = fields.ForeignKey(ContactoResource, 'contacto')
    proveedor = fields.ForeignKey(ProveedorResource, 'proveedor')

    class Meta:
        queryset = ContactosxProveedor.objects.all()
        resource_name = 'contactoproveedor'
        authorization = Authorization()