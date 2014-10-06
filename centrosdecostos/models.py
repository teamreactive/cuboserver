from django.db import models

from clientes.models import Cliente


class CentroDeCosto(models.Model):
    nombre = models.CharField(max_length=25)
    cliente = models.ForeignKey(Cliente)

    def __unicode__(self):
    	return '%s' % self.nombre

    class Meta:
        db_table = 'centro_de_costo'