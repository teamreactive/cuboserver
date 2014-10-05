from django.db import models


class Cliente(models.Model):
    nit = models.CharField(max_length=25)
    codigo_verificacion = models.CharField(max_length=25, null=True)
    razon_social = models.CharField(max_length=25)
    sigla = models.CharField(max_length=10, null=True)
    logo = models.ImageField(upload_to='logos', null=True)
