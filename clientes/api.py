from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from .models import Cliente


class ClienteResource(ModelResource):

    class Meta:
        queryset = Cliente.objects.all()
        resource_name = 'cliente'
        authorization = Authorization()