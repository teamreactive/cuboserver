from producto.api import ProductoResource
from proveedor.api import ProveedorResource
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from .models import Cotizacion


class CotizacionResource(ModelResource):
	producto = fields.ForeignKey(ProductoResource, 'producto')
	proveedor = fields.ForeignKey(ProveedorResource, 'proveedor')

    class Meta:
        queryset = Cotizacion.objects.all()
        resource_name = 'cotizacion'
        authorization = Authorization()