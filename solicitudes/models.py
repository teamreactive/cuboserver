from django.db import models

from datetime import datetime
from lugares.models import Lugar
from usuarios.models import Usuario
from centrosdecostos.models import CentroDeCosto
from equipos.models import Equipo
from productos.models import Producto, PrecioxProducto


class Solicitud(models.Model):
    ESTADOS = (
        ('1', 'solicitudud de compra creada'),
        ('2', 'solicitudud de compra rechazada'),
        ('3', 'solicitudud de compra aprobada'),
        ('4', 'cotizacion creada'),
    )
    estado = models.CharField(max_length=1, default='1', choices=ESTADOS)
    lugar_entrega = models.ForeignKey(Lugar, related_name='Solicitud.lugar_entrega')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_requerida = models.DateField()
    solicitante = models.ForeignKey(Usuario, related_name='Solicitud.solicitante')
    consolidador = models.ForeignKey(Usuario, related_name='Solicitud.consolidador', null=True)
    aprobador = models.ForeignKey(Usuario, related_name='Solicitud.aprobador', null=True)
    centro_de_costo = models.ForeignKey(CentroDeCosto, related_name='Solicitud.centro_de_costo', null=True)
    equipo = models.ForeignKey(Equipo, related_name='Solicitud.equipo', null=True)
    proyecto = models.CharField(max_length=25)
    productos = models.ManyToManyField(PrecioxProducto, through='ProductoXSolicitud')

    def __unicode__(self):
        return '%s - %s - %s' % (self.estado, self.solicitante, self.fecha_creacion)

    class Meta:
        db_table = 'solicitud'
class ProductoXSolicitud(models.Model):
    linea = models.IntegerField()
    producto = models.ForeignKey(PrecioxProducto)
    cantidad = models.DecimalField(max_digits=7, decimal_places=2)
    solicitud = models.ForeignKey(Solicitud)

    class Meta:
        unique_together = (
            ('linea'),('solicitud')
        )
