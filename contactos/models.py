from django.db import models


class Contacto(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    telefono_fijo = models.CharField(max_length=15, null=True)
    extension = models.CharField(max_length=5, null=True)
    celular = models.CharField(max_length=15, null=True)
    correo_electronico = models.EmailField(max_length=25, null=True)
    cargo = models.CharField(max_length=25, null=True)
    perfil = models.TextField(null=True)
