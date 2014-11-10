from django.db import models
from django.contrib.auth.models import User

from clientes.models import *
from contactos.models import *


class Usuario(models.Model):
	TIPOS = (
		("1", "administrador_general"),
		("2", "administrador_cliente"),
		("3", "solicitante"),
		("4", "codificador"),
		("5", "aprobador_solicitudes"),
		("6", "comprador"),
		("7", "aprobador_compra"),
		("8", "almacenista")
	)

	ACTIVOS = (
		("0", "no"),
		("1", "si")
	)

	nombre = models.CharField(max_length=20)
	password = models.CharField(max_length=112)
	cliente = models.ForeignKey(Cliente, related_name="Usuario.cliente", null=True)
	tipo = models.CharField(max_length=1, choices=TIPOS)
	contacto = models.ForeignKey(Contacto, related_name="Usuario.contacto")
	activo = models.CharField(max_length=1, choices=ACTIVOS)

	def __unicode__(self):
		return "%s %s" % (self.id, self.nombre)

	class Meta:
		db_table = "usuario"


class ConsolidadorSolicitante(models.Model):
	consolidador = models.ForeignKey(Usuario, related_name="ConsolidadorSolicitante.consolidador")
	solicitante = models.ForeignKey(Usuario, related_name="ConsolidadorSolicitante.solicitante")

	def __unicode__(self):
		return "%s %s" % (self.consolidador, self.solicitante)

	class Meta:
		db_table = "consolidadorsolicitante"


class SolicitanteCodificador(models.Model):
	solicitante = models.ForeignKey(Usuario, related_name="SolicitanteCodificador.solicitante")
	codificador = models.ForeignKey(Usuario, related_name="SolicitanteCodificador.codificador")

	def __unicode__(self):
		return "%s %s" % (self.solicitante, self.codificador)

	class Meta:
		db_table = "solicitantecodificador"


class AprobadorSolicitudesSolicitante(models.Model):
	aprobador = models.ForeignKey(Usuario, related_name="AprobadorSolicitudesSolicitante.aprobador")
	solicitante = models.ForeignKey(Usuario, related_name="AprobadorSolicitudesSolicitante.solicitante")

	def __unicode__(self):
		return "%s %s" % (self.aprobador, self.solicitante)

	class Meta:
		db_table = "aprobadorsolicitudessolicitante"


class AprobadorSolicitudesComprador(models.Model):
	aprobador = models.ForeignKey(Usuario, related_name="AprobadorSolicitudesComprador.aprobador")
	comprador = models.ForeignKey(Usuario, related_name="AprobadorSolicitudesComprador.comprador")

	def __unicode__(self):
		return "%s %s" % (self.aprobador, self.comprador)

	class Meta:
		db_table = "aprobadorsolicitudescomprador"


class CompradorAprobadorCompras(models.Model):
	aprobador = models.ForeignKey(Usuario, related_name="CompradorAprobadorCompras.aprobador")
	comprador = models.ForeignKey(Usuario, related_name="CompradorAprobadorCompras.comprador")

	def __unicode__(self):
		return "%s %s" % (self.aprobador, self.comprador)

	class Meta:
		db_table = "compradoraprobadorcompras"


class AprobadorCompraAlmacenista(models.Model):
	aprobador = models.ForeignKey(Usuario, related_name="AprobadorCompraAlmacenista.aprobador")
	almacenista = models.ForeignKey(Usuario, related_name="AprobadorCompraAlmacenista.almacenista")

	def __unicode__(self):
		return "%s %s" % (self.aprobador, self.almacenista)

	class Meta:
		db_table = "aprobadorcomprasalmacenista"