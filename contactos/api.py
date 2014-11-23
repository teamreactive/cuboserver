from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from .models import *


class ContactoResource(ModelResource):

	class Meta:
		queryset = Contacto.objects.all()
		resource_name = "contacto"
		authorization = Authorization()