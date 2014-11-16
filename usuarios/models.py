from django.db import models
from django.contrib.auth.models import User
from hashlib import *

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
	password = models.CharField(max_length=130)
	cliente = models.ForeignKey(Cliente, related_name="Usuario.cliente", null=True)
	tipo = models.CharField(max_length=1, choices=TIPOS)
	contacto = models.ForeignKey(Contacto, related_name="Usuario.contacto", null=True)
	activo = models.CharField(max_length=1, choices=ACTIVOS)

	def save(self, *args, **kwargs):
		self.id = 1
		self.password = sha512(self.password).hexdigest()
		try: self.id = Usuario.objects.all().order_by("-id")[0].id + 1
		except: pass
		super(Usuario, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.id, self.nombre)

	class Meta:
		db_table = "usuario"


class ConsolidadorSolicitante(models.Model):
	consolidador = models.ForeignKey(Usuario, related_name="ConsolidadorSolicitante.consolidador")
	solicitante = models.ForeignKey(Usuario, related_name="ConsolidadorSolicitante.solicitante")

	def save(self, *args, **kwargs):
		self.id = 1
		try: self.id = ConsolidadorSolicitante.objects.all().order_by("-id")[0].id + 1
		except: pass
		super(ConsolidadorSolicitante, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.consolidador, self.solicitante)

	class Meta:
		db_table = "consolidadorsolicitante"


class SolicitanteCodificador(models.Model):
	solicitante = models.ForeignKey(Usuario, related_name="SolicitanteCodificador.solicitante")
	codificador = models.ForeignKey(Usuario, related_name="SolicitanteCodificador.codificador")

	def save(self, *args, **kwargs):
		self.id = 1
		try: self.id = SolicitanteCodificador.objects.all().order_by("-id")[0].id + 1
		except: pass
		super(SolicitanteCodificador, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.solicitante, self.codificador)

	class Meta:
		db_table = "solicitantecodificador"


class AprobadorSolicitudesSolicitante(models.Model):
	aprobador = models.ForeignKey(Usuario, related_name="AprobadorSolicitudesSolicitante.aprobador")
	solicitante = models.ForeignKey(Usuario, related_name="AprobadorSolicitudesSolicitante.solicitante")

	def save(self, *args, **kwargs):
		self.id = 1
		try: self.id = AprobadorSolicitudesSolicitante.objects.all().order_by("-id")[0].id + 1
		except: pass
		super(AprobadorSolicitudesSolicitante, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.aprobador, self.solicitante)

	class Meta:
		db_table = "aprobadorsolicitudessolicitante"


class AprobadorSolicitudesComprador(models.Model):
	aprobador = models.ForeignKey(Usuario, related_name="AprobadorSolicitudesComprador.aprobador")
	comprador = models.ForeignKey(Usuario, related_name="AprobadorSolicitudesComprador.comprador")

	def save(self, *args, **kwargs):
		self.id = 1
		try: self.id = AprobadorSolicitudesComprador.objects.all().order_by("-id")[0].id + 1
		except: pass
		super(AprobadorSolicitudesComprador, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.aprobador, self.comprador)

	class Meta:
		db_table = "aprobadorsolicitudescomprador"


class CompradorAprobadorCompras(models.Model):
	aprobador = models.ForeignKey(Usuario, related_name="CompradorAprobadorCompras.aprobador")
	comprador = models.ForeignKey(Usuario, related_name="CompradorAprobadorCompras.comprador")

	def save(self, *args, **kwargs):
		self.id = 1
		try: self.id = CompradorAprobadorCompras.objects.all().order_by("-id")[0].id + 1
		except: pass
		super(CompradorAprobadorCompras, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.aprobador, self.comprador)

	class Meta:
		db_table = "compradoraprobadorcompras"


class AprobadorComprasAlmacenista(models.Model):
	aprobador = models.ForeignKey(Usuario, related_name="AprobadorComprasAlmacenista.aprobador")
	almacenista = models.ForeignKey(Usuario, related_name="AprobadorComprasAlmacenista.almacenista")

	def save(self, *args, **kwargs):
		self.id = 1
		try: self.id = AprobadorComprasAlmacenista.objects.all().order_by("-id")[0].id + 1
		except: pass
		super(AprobadorComprasAlmacenista, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" % (self.aprobador, self.almacenista)

	class Meta:
		db_table = "aprobadorcomprasalmacenista"