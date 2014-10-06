# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


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
<<<<<<< HEAD
            name='ProductosxSolicitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_linea', models.IntegerField()),
                ('cantidad_producto', models.DecimalField(max_digits=10, decimal_places=2)),
                ('unidad_producto', models.CharField(max_length=15)),
                ('producto', models.ForeignKey(related_name=b'PxS.producto', to='productos.Producto')),
            ],
            options={
                'db_table': 'producto_por_solicitud',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
=======
>>>>>>> ad787553272f977a8eacb6148a6435f10de128d4
            name='Solicitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(max_length=1)),
                ('fecha_creacion', models.DateTimeField(default=datetime.datetime.now)),
                ('fecha_requerida', models.DateTimeField()),
                ('proyecto', models.CharField(max_length=25)),
                ('aprobador', models.ForeignKey(related_name=b'Solicitud.aprobador', to='usuarios.Usuario', null=True)),
                ('centro_de_costo', models.ForeignKey(related_name=b'Solicitud.centro_de_costo', to='centrosdecostos.CentroDeCosto', null=True)),
                ('consolidador', models.ForeignKey(related_name=b'Solicitud.consolidador', to='usuarios.Usuario', null=True)),
                ('equipo', models.ForeignKey(related_name=b'Solicitud.equipo', to='equipos.Equipo', null=True)),
                ('lugar_entrega', models.ForeignKey(related_name=b'Solicitud.lugar_entrega', to='lugares.Lugar')),
                ('productos', models.ManyToManyField(to='productos.Producto', db_table=b'productosxsolicitud')),
                ('solicitante', models.ForeignKey(related_name=b'Solicitud.solicitante', to='usuarios.Usuario')),
            ],
            options={
                'db_table': 'solicitud',
            },
            bases=(models.Model,),
        ),
    ]
