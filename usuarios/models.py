from django.db import models

from clientes.models import Cliente
from contactos.models import Contacto


class Usuario(models.Model):
    TIPOS = (
        ('1', 'administrador_general'),
        ('2', 'administrador_cliente'),
        ('3', 'solicitante'),
        ('4', 'codificador'),
        ('5', 'aprobador_solicitudes'),
        ('6', 'comprador'),
        ('7', 'aprobador_compra'),
        ('8', 'almacenista'),
    )
    ACTIVOS = (
        ('0', 'no'),
        ('1', 'si'),
    )
    nombre = models.CharField(max_length=25, primary_key=True)
    contrasena = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, related_name='Usuario.cliente', null=True)
    tipo = models.CharField(max_length=1, choices=TIPOS)
    contacto = models.ForeignKey(Contacto, related_name='Usuario.contacto')
    activo = models.CharField(max_length=1, choices=ACTIVOS)

    def __unicode__(self):
        return '%s' % self.nombre

    class Meta:
        db_table = 'usuario'

class ConsolidadorxSolicitante(models.Model):
    consolidador = models.ForeignKey(Usuario, related_name='CxS.consolidador')
    solicitante = models.ForeignKey(Usuario, related_name='CxS.solicitante')

    class Meta:
        db_table = 'consolidador_por_solicitante'

class SolicitantexCodificador(models.Model):
    solicitante = models.ForeignKey(Usuario, related_name='SxC.solicitante')
    codificador = models.ForeignKey(Usuario, related_name='SxC.codificador')

    class Meta:
        db_table = 'solicitante_por_codificador'

class AprobadorSolicitudesxSolicitante(models.Model):
    aprobador = models.ForeignKey(Usuario, related_name='ASxS.aprobador')
    solicitante = models.ForeignKey(Usuario, related_name='ASxS.solicitante')

    class Meta:
        db_table = 'aprobador_solicitudes_por_solicitante'

class AprobadorSolicitudesxComprador(models.Model):
    aprobador = models.ForeignKey(Usuario, related_name='ASxC.aprobador')
    comprador = models.ForeignKey(Usuario, related_name='ASxC.comprador')

    class Meta:
        db_table = 'aprobador_solicitudes_por_comprador'

class CompradorxAprobadorCompras(models.Model):
    aprobador = models.ForeignKey(Usuario, related_name='CxAC.aprobador')
    comprador = models.ForeignKey(Usuario, related_name='CxAC.comprador')

    class Meta:
        db_table = 'comprador_por_aprobador_compras'

class AprobadorCompraxAlmacenista(models.Model):
    aprobador = models.ForeignKey(Usuario, related_name='ACxA.aprobador')
    almacenista = models.ForeignKey(Usuario, related_name='ACxA.almacenista')

    class Meta:
        db_table = 'aprobador_compras_por_almacenista'