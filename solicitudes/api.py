from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from centros.api import *
from equipos.api import *
from lugares.api import *
from .models import *
from productos.api import *
from usuarios.api import *


class ProductoSolicitudResource(ModelResource):
	producto = fields.ForeignKey(ProductoResource, "producto")

	class Meta:
		queryset = ProductoSolicitud.objects.all()
		resource_name = "productosolicitud"
		authorization = Authorization()


class SolicitudResource(ModelResource):
	lugar = fields.ForeignKey(LugarResource, "lugar", full=True)
	solicitante = fields.ForeignKey(UsuarioResource, "solicitante")
	consolidador = fields.ForeignKey(UsuarioResource, "consolidador", null=True)
	aprobador = fields.ForeignKey(UsuarioResource, "aprobador", null=True)
	centro = fields.ForeignKey(CentroResource, "centro", null=True)
	equipo =  fields.ForeignKey(EquipoResource, "equipo", null=True)
	productos = fields.ToManyField(ProductoSolicitudResource, "productos", full=True)

	class Meta:
		queryset = Solicitud.objects.all()
		resource_name = "solicitud"
		authorization = Authorization()
		filtering = {
			"estado": ("exact"),
			"solicitante": ("exact")
		}