from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from centros.api import *
from equipos.api import *
from lugares.api import *
from .models import *
from productos.api import *
from usuarios.api import *


class SolicitudResource(ModelResource):
	lugar = fields.ForeignKey(LugarResource, "lugar")
	solicitante = fields.ForeignKey(UsuarioResource, "solicitante")
	consolidador = fields.ForeignKey(UsuarioResource, "consolidador")
	aprobador = fields.ForeignKey(UsuarioResource, "aprobador")
	centro = fields.ForeignKey(CentroResource, "centro")
	equipo =  fields.ForeignKey(EquipoResource, "equipo")

	class Meta:
		queryset = Solicitud.objects.all()
		resource_name = "solicitud"
		authorization = Authorization()
		filtering = {
			"solicitante": ("exact")
		}


class ProductoSolicitudResource(ModelResource):
	producto = fields.ForeignKey(UnidadProductoResource, "producto")
	solicitud = fields.ForeignKey(SolicitudResource, "solicitud")

	class Meta:
		queryset = ProductoSolicitud.objects.all()
		resource_name = "productosolicitud"
		authorization = Authorization()