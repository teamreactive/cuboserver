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
                ('fechaentregado', models.DateTimeField(default=datetime.datetime.now)),
                ('entregaparcial', models.DateTimeField(default=datetime.datetime.now)),
                ('porcentajedevolucion', models.DecimalField(max_digits=5, decimal_places=2)),
                ('cotizacion', models.ForeignKey(related_name=b'Compra.cotizacion', to='cotizaciones.Cotizacion')),
            ],
            options={
                'db_table': 'compra',
            },
            bases=(models.Model,),
        ),
    ]
