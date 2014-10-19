# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_remove_precioxproducto_precio_promedio'),
        ('solicitudes', '0003_auto_20141006_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoXSolicitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=7, decimal_places=2)),
                ('producto', models.ForeignKey(to='productos.PrecioxProducto')),
                ('solicitud', models.ForeignKey(to='solicitudes.Solicitud')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='productos',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='productos',
            field=models.ManyToManyField(to=b'productos.PrecioxProducto', through='solicitudes.ProductoXSolicitud'),
        ),
    ]
