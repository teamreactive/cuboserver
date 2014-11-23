from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.resources import ModelResource

from .models import *


class ClienteResource(ModelResource):

	class Meta:
		queryset = Cliente.objects.all()
		resource_name = "cliente"
		authorization = Authorization()