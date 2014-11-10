# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productoxsolicitud',
            name='estado',
            field=models.CharField(default=b'', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productoxsolicitud',
            name='producto',
            field=models.ForeignKey(to='productos.UnidadXProducto'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='productos',
            field=models.ManyToManyField(to=b'productos.UnidadXProducto', through='solicitudes.ProductoXSolicitud'),
        ),
    ]
