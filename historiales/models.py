from django.db import models

from usuarios.models import Usuario

from datetime import datetime


class Historial(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='Historial.usuario')
    fecha = models.DateTimeField(default=datetime.now)
    descripcion = models.TextField()

    class Meta:
        db_table = 'historial'