from django.db import models

from centrosdecostos.models import CentroDeCosto
from clientes.models import Cliente
from contactos.models import Contacto
from equipos.models import Equipo
from familiasproveedores.models import FamiliaProveedor


class Producto(models.Model):
    codigo_onu = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField(null=True,blank=True)
    referencia = models.CharField(max_length=25, null=True,blank=True)
    marca = models.CharField(max_length=25)
    servicio = models.BooleanField(default=False)
    familia_proveedor = models.ForeignKey(FamiliaProveedor, null=True)
    tiempo_promedio = models.CharField(max_length=15, null=True, blank=True)
    cliente = models.ForeignKey(Cliente)
    contacto_novende = models.ManyToManyField(Contacto,dt_table='ProductoxContactoQueNoVende')
    contacto_vende = models.ManyToManyField(Contacto,dt_table='ProductoxContactoQueVende')
    class Meta:
        db_table = 'producto'

class NombresxProducto(models.Model):
    producto = models.ForeignKey(Producto)
    nombre = models.CharField(max_length=25)

    class Meta:
        db_table = 'nombre_por_contacto'

class FotosxProducto(models.Model):
    producto = models.ForeignKey(Producto)
    foto = models.CharField(max_length=100)

    class Meta:
        db_table = 'fotos_por_producto'

class PrecioxProducto(models.Model):
    producto = models.ForeignKey(Producto)
    unidad = models.CharField(max_length=1)
    talla = models.CharField(max_length=1)
    precio_promedio = models.FloatField(null=True)

    class Meta:
        db_table = 'precio_producto'
