from django.db import models


class Cliente(models.Model):
    nit = models.CharField(max_length=25, unique=True)
    codigo_verificacion = models.CharField(max_length=25, null=True, blank=True, unique=True)
    razon_social = models.CharField(max_length=25, unique=True)
    sigla = models.CharField(max_length=10, null=True, blank=True)
    logo = models.ImageField(upload_to='logos', null=True, blank=True)

    def __unicode__(self):
        return self.nit

    class Meta:
        db_table = 'cliente'
