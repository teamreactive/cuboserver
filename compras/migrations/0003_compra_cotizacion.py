# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0009_crear'),
        ('compras', '0002_compra_cotizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='cotizacion',
            field=models.ForeignKey(related_name=b'Compra.cotizacion', to='cotizaciones.Cotizacion', null=True),
            preserve_default=True,
        ),
    ]
