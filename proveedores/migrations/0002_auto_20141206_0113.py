# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='nit',
            field=common.upper.UpperCharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='razon',
            field=common.upper.UpperCharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='sigla',
            field=common.upper.UpperCharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='verificacion',
            field=common.upper.UpperCharField(max_length=25),
        ),
    ]
