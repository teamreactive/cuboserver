from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from common.api import *
from .models import *


class ContactoResource(CORSResource, ModelResource):

	class Meta:
		queryset = Contacto.objects.all()
		resource_name = "contacto"
		authorization = Authorization()