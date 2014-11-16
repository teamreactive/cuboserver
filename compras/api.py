from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from cotizaciones.api import *
from .models import *


class CompraResource(ModelResource):
	cotizacion = fields.ForeignKey(CotizacionResource, "cotizacion")

	class Meta:
		queryset = Compra.objects.all()
		resource_name = "cotizacion"
		authorization = Authorization()