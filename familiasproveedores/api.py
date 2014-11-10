from clientes.api import ClienteResource
from contactos.api import ContactoResource
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource
from .models import FamiliaProveedor


class FamiliaResource(ModelResource):
    cliente = fields.ForeignKey(ClienteResource, 'cliente')
    contactos = fields.ToManyField(ContactoResource, 'contactos')

    class Meta:
        queryset = FamiliaProveedor.objects.all()
        resource_name = 'familia'
        authorization = Authorization()