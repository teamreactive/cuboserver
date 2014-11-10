# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0001_initial'),
        ('usuarios', '0001_initial'),
        ('equipos', '0001_initial'),
        ('centros', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoSolicitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('linea', models.IntegerField()),
                ('cantidad', models.DecimalField(max_digits=7, decimal_places=2)),
                ('estado', models.CharField(default=b'', max_length=20)),
                ('producto', models.ForeignKey(related_name=b'ProductoSolicitud.producto', to='productos.UnidadProducto')),
            ],
            options={
                'db_table': 'productosolicitud',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'solicitudud de compra creada'), (b'2', b'solicitudud de compra rechazada'), (b'3', b'solicitudud de compra aprobada'), (b'4', b'cotizacion creada')])),
                ('fechacreacion', models.DateTimeField(auto_now_add=True)),
                ('fecharequerida', models.DateField()),
                ('proyecto', models.CharField(max_length=25)),
                ('aprobador', models.ForeignKey(related_name=b'Solicitud.aprobador', to='usuarios.Usuario', null=True)),
                ('centro', models.ForeignKey(related_name=b'Solicitud.centro', to='centros.Centro', null=True)),
                ('consolidador', models.ForeignKey(related_name=b'Solicitud.consolidador', to='usuarios.Usuario', null=True)),
                ('equipo', models.ForeignKey(related_name=b'Solicitud.equipo', to='equipos.Equipo', null=True)),
                ('lugar', models.ForeignKey(related_name=b'Solicitud.lugar', to='lugares.Lugar')),
                ('productos', models.ManyToManyField(related_name=b'Solicitud.productos', through='solicitudes.ProductoSolicitud', to='productos.UnidadProducto')),
                ('solicitante', models.ForeignKey(related_name=b'Solicitud.solicitante', to='usuarios.Usuario')),
            ],
            options={
                'db_table': 'solicitud',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='productosolicitud',
            name='solicitud',
            field=models.ForeignKey(related_name=b'ProductoSolicitud.solicitud', to='solicitudes.Solicitud'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='productosolicitud',
            unique_together=set([('linea', 'solicitud')]),
        ),
    ]
