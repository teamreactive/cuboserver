from centrosdecostos.api import CentroResource
from equipos.api import EquipoResource
from lugares.api import LugarResource
from productos.api import UnidadProductoResource
from usuarios.api import UsuarioResource
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from .models import *


class SolicitudResource(ModelResource):
    lugar_entrega = fields.ForeignKey(LugarResource, 'lugar_entrega')
    solicitante = fields.ForeignKey(UsuarioResource, 'solicitante')
    consolidador = fields.ForeignKey(UsuarioResource, 'consolidador')
    aprobador = fields.ForeignKey(UsuarioResource, 'aprobador')
    centro_de_costo = fields.ForeignKey(CentroResource, 'centro_de_costo')
    equipo =  fields.ForeignKey(EquipoResource, 'equipo')

    class Meta:
        queryset = solicitud.objects.all()
        resource_name = 'solicitud'
        authorization = Authorization()


class ProductoSolicitudResource(ModelResource):
    producto = fields.ForeignKey(UnidadProductoResource, 'producto')
    solicitud = fields.ForeignKey(SolicitudResource, 'solicitud')

    class Meta:
        queryset = ProductoXSolicitud.objects.all()
        resource_name = 'productosolicitud'
        authorization = Authorization()