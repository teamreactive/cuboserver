# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='formapago',
            field=common.upper.UpperCharField(max_length=1, choices=[(b'1', b'anticipado'), (b'2', b'contado'), (b'3', b'dias')]),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='iva',
            field=common.upper.UpperCharField(max_length=1, choices=[(b'1', b'16'), (b'2', b'1.6'), (b'3', b'20'), (b'4', b'0')]),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='referencia',
            field=common.upper.UpperCharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='validez',
            field=common.upper.UpperCharField(max_length=25),
        ),
    ]
