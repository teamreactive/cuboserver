from clientes.api import ClienteResource
from contactos.api import ContactoResource
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from .models import *


class UsuarioResource(ModelResource):
    cliente = fields.ForeignKey(ClienteResource, 'cliente')
    contacto = fields.ForeignKey(ContactoResource, 'contacto')

    class Meta:
        queryset = Usuario.objects.all()
        resource_name = 'usuario'
        authorization = Authorization()


class ConsolidadorSolicitanteResource(ModelResource):
    consolidador = fields.ForeignKey(UsuarioResource, 'consolidador')
    solicitante = fields.ForeignKey(UsuarioResource, 'solicitante')

    class Meta:
        queryset = ConsolidadorxSolicitante.objects.all()
        resource_name = 'consolidadorsolicitante'
        authorization = Authorization()


class SolicitanteCodificadorResource(ModelResource):
    solicitante = fields.ForeignKey(UsuarioResource, 'solicitante')
    codificador = fields.ForeignKey(UsuarioResource, 'codificador')

    class Meta:
        queryset = SolicitantexCodificador.objects.all()
        resource_name = 'solicitantecodificador'
        authorization = Authorization()


class AprobadorSolicitudesSolicitanteResource(ModelResource):
    aprobador = fields.ForeignKey(UsuarioResource, 'aprobador')
    solicitante = fields.ForeignKey(UsuarioResource, 'solicitante')

    class Meta:
        queryset = AprobadorSolicitudesxSolicitante.objects.all()
        resource_name = 'aprobadorsolicitudessolicitante'
        authorization = Authorization()


class AprobadorSolicitudesCompradorResource(ModelResource):
    aprobador = fields.ForeignKey(UsuarioResource, 'aprobador')
    comprador = fields.ForeignKey(UsuarioResource, 'comprador')

    class Meta:
        queryset = AprobadorSolicitudesxComprador.objects.all()
        resource_name = 'aprobadorsolicitudescomprador'
        authorization = Authorization()


class CompradorAprobadorComprasResource(ModelResource):
    aprobador = fields.ForeignKey(UsuarioResource, 'aprobador')
    comprador = fields.ForeignKey(UsuarioResource, 'comprador')

    class Meta:
        queryset = CompradorxAprobadorCompras.objects.all()
        resource_name = 'compradoraprobadorcompras'
        authorization = Authorization()


class AprobadorComprasAlmacenistaResource(ModelResource):
    aprobador = fields.ForeignKey(UsuarioResource, 'aprobador')
    almacenista = fields.ForeignKey(UsuarioResource, 'almacenista')

    class Meta:
        queryset = AprobadorCompraxAlmacenista.objects.all()
        resource_name = 'aprobadorcomprasalmacenista'
        authorization = Authorization()