# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0002_auto_20141112_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productosolicitud',
            name='estado',
            field=common.upper.UpperCharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='estado',
            field=common.upper.UpperCharField(default=b'1', max_length=1, choices=[(b'1', b'solicitudud de compra creada'), (b'2', b'solicitudud de compra rechazada'), (b'3', b'solicitudud de compra aprobada'), (b'4', b'cotizacion creada')]),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='proyecto',
            field=common.upper.UpperCharField(max_length=25),
        ),
    ]
