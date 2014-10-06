# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='estado',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'1', b'solicitudud de compra creada'), (b'2', b'solicitudud de compra rechazada'), (b'3', b'solicitudud de compra aprobada'), (b'4', b'cotizacion creada')]),
        ),
    ]
