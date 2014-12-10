# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaentregado', models.DateTimeField(default=datetime.datetime.now)),
                ('entregaparcial', models.DateTimeField(default=datetime.datetime.now)),
                ('porcentajedevolucion', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
            options={
                'db_table': 'compra',
            },
            bases=(models.Model,),
        ),
    ]
