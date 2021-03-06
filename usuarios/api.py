from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from common.api import *
from clientes.api import *
from contactos.api import *
from .models import *


class UsuarioResource(CORSResource, ModelResource):
	cliente = fields.ForeignKey(ClienteResource, "cliente", null=True)
	contacto = fields.ForeignKey(ContactoResource, "contacto", null=True, full=True)

	class Meta:
		queryset = Usuario.objects.all()
		resource_name = "usuario"
		authorization = Authorization()
		filtering = {
			"nombre": ("exact")
		}


class ConsolidadorSolicitanteResource(ModelResource):
	consolidador = fields.ForeignKey(UsuarioResource, "consolidador")
	solicitante = fields.ForeignKey(UsuarioResource, "solicitante")

	class Meta:
		queryset = ConsolidadorSolicitante.objects.all()
		resource_name = "consolidadorsolicitante"
		authorization = Authorization()


class SolicitanteCodificadorResource(ModelResource):
	solicitante = fields.ForeignKey(UsuarioResource, "solicitante")
	codificador = fields.ForeignKey(UsuarioResource, "codificador")

	class Meta:
		queryset = SolicitanteCodificador.objects.all()
		resource_name = "solicitantecodificador"
		authorization = Authorization()


class AprobadorSolicitudesSolicitanteResource(ModelResource):
	aprobador = fields.ForeignKey(UsuarioResource, "aprobador")
	solicitante = fields.ForeignKey(UsuarioResource, "solicitante")

	class Meta:
		queryset = AprobadorSolicitudesSolicitante.objects.all()
		resource_name = "aprobadorsolicitudessolicitante"
		authorization = Authorization()


class AprobadorSolicitudesCompradorResource(ModelResource):
	aprobador = fields.ForeignKey(UsuarioResource, "aprobador")
	comprador = fields.ForeignKey(UsuarioResource, "comprador")

	class Meta:
		queryset = AprobadorSolicitudesComprador.objects.all()
		resource_name = "aprobadorsolicitudescomprador"
		authorization = Authorization()


class CompradorAprobadorComprasResource(ModelResource):
	aprobador = fields.ForeignKey(UsuarioResource, "aprobador")
	comprador = fields.ForeignKey(UsuarioResource, "comprador")

	class Meta:
		queryset = CompradorAprobadorCompras.objects.all()
		resource_name = "compradoraprobadorcompras"
		authorization = Authorization()


class AprobadorComprasAlmacenistaResource(ModelResource):
	aprobador = fields.ForeignKey(UsuarioResource, "aprobador")
	almacenista = fields.ForeignKey(UsuarioResource, "almacenista")

	class Meta:
		queryset = AprobadorComprasAlmacenista.objects.all()
		resource_name = "aprobadorcomprasalmacenista"
		authorization = Authorization()