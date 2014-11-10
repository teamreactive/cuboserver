from proveedores.api import ProveedorResource
from solicitudes.api import ProductoSolicitudResource
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource
from .models import Cotizacion


class CotizacionResource(ModelResource):
    producto = fields.ForeignKey(ProductoSolicitudResource, 'producto')
    proveedor = fields.ForeignKey(ProveedorResource, 'proveedor')

    class Meta:
        queryset = Cotizacion.objects.all()
        resource_name = 'cotizacion'
        authorization = Authorization()