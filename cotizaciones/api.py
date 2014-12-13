from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from .models import *
from proveedores.api import *
from productos.api import *


class CotizacionResource(ModelResource):
	producto = fields.ForeignKey(ProductoResource, "producto")
	proveedor = fields.ForeignKey(ProveedorResource, "proveedor")

	class Meta:
		queryset = Cotizacion.objects.all()
		resource_name = "cotizacion"
		authorization = Authorization()