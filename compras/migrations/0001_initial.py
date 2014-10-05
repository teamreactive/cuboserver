# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_entregado', models.DateTimeField(default=datetime.datetime.now)),
                ('entrega_parcial', models.DateTimeField(default=datetime.datetime.now)),
                ('porcentaje_de_devolucion', models.DecimalField(max_digits=5, decimal_places=2)),
                ('cotizacion', models.ForeignKey(to='cotizaciones.Cotizacion')),
            ],
            options={
                'db_table': 'compra',
            },
            bases=(models.Model,),
        ),
    ]
