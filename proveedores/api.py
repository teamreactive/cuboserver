from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from lugares.api import *
from .models import *


class ProveedorResource(ModelResource):
	lugar = fields.ForeignKey(LugarResource, "lugar", full=True)

	class Meta:
		queryset = Proveedor.objects.all()
		resource_name = "proveedor"
		authorization = Authorization()