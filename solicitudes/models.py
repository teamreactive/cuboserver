from django.db import models

from datetime import datetime
from lugares.models import Lugar
from usuarios.models import Usuario
from centrosdecostos.models import CentroDeCosto
from equipos.models import Equipo
from productos.models import Producto


class Solicitud(models.Model):
    EMERGENCIAS = (
        ('0', 'no'),
        ('1', 'si'),
    )
    estado = models.CharField(max_length=1)
    lugar_entrega = models.ForeignKey(Lugar, related_name='Solicitud.lugar_entrega')
    fecha_creacion = models.DateTimeField(default=datetime.now)
    fecha_requerida = models.DateTimeField()
    solicitante = models.ForeignKey(Usuario, related_name='Solicitud.solicitante')
    consolidador = models.ForeignKey(Usuario, related_name='Solicitud.consolidador', null=True)
    aprobador = models.ForeignKey(Usuario, related_name='Solicitud.aprobador', null=True)
    centro_de_costo = models.ForeignKey(CentroDeCosto, related_name='Solicitud.centro_de_costo', null=True)
    equipo = models.ForeignKey(Equipo, related_name='Solicitud.equipo', null=True)
    emergencia = models.CharField(max_length=1, choices=EMERGENCIAS)
    proyecto = models.CharField(max_length=25)

class ProductosxSolicitud(models.Model):
    solicitud = models.ForeignKey(Solicitud, related_name='PxS.solicitud')
    producto = models.ForeignKey(Producto, related_name='PxS.producto')
    numero_linea = models.IntegerField()
    cantidad_producto = models.DecimalField(max_digits=10, decimal_places=2)
    unidad_producto = models.CharField(max_length=15)
