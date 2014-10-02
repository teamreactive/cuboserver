from django.db import models

from datetime import datetime
from cotizaciones.models import Cotizacion


class Compra(models.Model):
    cotizacion = models.ForeignKey(Cotizacion)
    fecha_entregado = models.DateTimeField(default=datetime.now)
    entrega_parcial = models.DateTimeField(default=datetime.now)
    porcentaje_de_devolucion = models.CharField(max_length=5)