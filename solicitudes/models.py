from django.db import models

from datetime import datetime
from lugares.models import Lugar
from usuarios.models import Usuario
from centrosdecostos.models import CentroDeCosto
from equipos.models import Equipo
from productos.models import Producto


class Solicitud(models.Model):
    ESTADOS = (
        ('1','solicitado'),
        ('2','rechazado por aprobador de solicitudes'),
        ('3'.'apro'))
    estado = models.CharField(max_length=1, choices=ESTADOS)
    lugar_entrega = models.ForeignKey(Lugar, related_name='Solicitud.lugar_entrega')
    fecha_creacion = models.DateTimeField(default=datetime.now)
    fecha_requerida = models.DateTimeField()
    solicitante = models.ForeignKey(Usuario, related_name='Solicitud.solicitante')
    consolidador = models.ForeignKey(Usuario, related_name='Solicitud.consolidador', null=True)
    aprobador = models.ForeignKey(Usuario, related_name='Solicitud.aprobador', null=True)
    centro_de_costo = models.ForeignKey(CentroDeCosto, related_name='Solicitud.centro_de_costo', null=True)
    equipo = models.ForeignKey(Equipo, related_name='Solicitud.equipo', null=True)
    proyecto = models.CharField(max_length=25)
    productos = models.ManyToManyField(Producto, db_table='productosxsolicitud')

    class Meta:
        db_table = 'solicitud'