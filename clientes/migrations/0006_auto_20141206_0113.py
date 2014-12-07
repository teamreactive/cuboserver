# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20141110_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nit',
            field=common.upper.UpperCharField(unique=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='razon',
            field=common.upper.UpperCharField(unique=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sigla',
            field=common.upper.UpperCharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='verificacion',
            field=common.upper.UpperCharField(max_length=25, unique=True, null=True, blank=True),
        ),
    ]
