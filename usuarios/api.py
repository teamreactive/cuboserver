from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource

from .models import *


class UsuarioResource(ModelResource):
	cliente = fields.ForeignKey("clientes.api.ClienteResource", "cliente")

	class Meta:
		queryset = Usuario.objects.all()
		resource_name = "usuario"
		authorization = Authorization()
		always_return_data = True
		filtering = {
			"cliente": ("exact"),
			"usuario": ("exact")
		}


class ConsolidadorSolicitanteResource(ModelResource):
	consolidador = fields.ForeignKey(UsuarioResource, "consolidador")
	solicitante = fields.ForeignKey(UsuarioResource, "solicitante")

	class Meta:
		queryset = ConsolidadorSolicitante.objects.all()
		resource_name = "consolidadorsolicitante"
		authorization = Authorization()
		filtering = {
			"consolidador": ("exact"),
			"solicitante": ("exact")
		}


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
		filtering = {
			"aprobador": ("exact"),
			"solicitante": ("exact")
		}


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