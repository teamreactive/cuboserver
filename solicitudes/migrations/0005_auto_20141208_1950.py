# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0004_auto_20141208_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productosolicitud',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='productosolicitud',
            name='solicitud',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='productos',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='productoss',
            field=models.ManyToManyField(related_name=b'Solicitud.productos', to='solicitudes.ProductoSolicitud'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productosolicitud',
            name='producto',
            field=models.ForeignKey(related_name=b'ProductoSolicitud.producto', to='productos.Producto'),
        ),
    ]
