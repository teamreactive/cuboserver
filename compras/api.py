from cotizacion.api import CotizacionResource
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from .models import Compra


class CompraResource(ModelResource):
    cotizacion = fields.ForeignKey(CotizacionResource, 'cotizacion')

    class Meta:
        queryset = Compra.objects.all()
        resource_name = 'cotizacion'
        authorization = Authorization()