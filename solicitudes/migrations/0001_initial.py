# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0001_initial'),
        ('usuarios', '0001_initial'),
        ('equipos', '0001_initial'),
        ('centrosdecostos', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoXSolicitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('linea', models.IntegerField()),
                ('cantidad', models.DecimalField(max_digits=7, decimal_places=2)),
                ('producto', models.ForeignKey(to='productos.PrecioxProducto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'solicitudud de compra creada'), (b'2', b'solicitudud de compra rechazada'), (b'3', b'solicitudud de compra aprobada'), (b'4', b'cotizacion creada')])),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_requerida', models.DateField()),
                ('proyecto', models.CharField(max_length=25)),
                ('aprobador', models.ForeignKey(related_name=b'Solicitud.aprobador', to='usuarios.Usuario', null=True)),
                ('centro_de_costo', models.ForeignKey(related_name=b'Solicitud.centro_de_costo', to='centrosdecostos.CentroDeCosto', null=True)),
                ('consolidador', models.ForeignKey(related_name=b'Solicitud.consolidador', to='usuarios.Usuario', null=True)),
                ('equipo', models.ForeignKey(related_name=b'Solicitud.equipo', to='equipos.Equipo', null=True)),
                ('lugar_entrega', models.ForeignKey(related_name=b'Solicitud.lugar_entrega', to='lugares.Lugar')),
                ('productos', models.ManyToManyField(to='productos.PrecioxProducto', through='solicitudes.ProductoXSolicitud')),
                ('solicitante', models.ForeignKey(related_name=b'Solicitud.solicitante', to='usuarios.Usuario')),
            ],
            options={
                'db_table': 'solicitud',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='productoxsolicitud',
            name='solicitud',
            field=models.ForeignKey(to='solicitudes.Solicitud'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='productoxsolicitud',
            unique_together=set([('linea', 'solicitud')]),
        ),
    ]
