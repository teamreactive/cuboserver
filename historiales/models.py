from django.db import models

from datetime import datetime


class Historial(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='Historial.usuario')
    fecha = models.DateTimeField(default=datetime.now)
    descripcion = models.TextField()