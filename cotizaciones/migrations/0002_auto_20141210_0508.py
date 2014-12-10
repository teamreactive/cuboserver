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
            field=common.upper.UpperCharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='referencia',
            field=common.upper.UpperCharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='validez',
            field=common.upper.UpperCharField(max_length=50),
        ),
    ]
