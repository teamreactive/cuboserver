# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='producto',
            field=models.ForeignKey(to='solicitudes.ProductoXSolicitud', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
