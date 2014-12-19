# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0005_auto_20141216_0633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='lugar',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='ciudad',
            field=common.upper.UpperCharField(default='BOGOTA', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='numero1',
            field=common.upper.UpperCharField(default=166, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='numero2',
            field=common.upper.UpperCharField(default=32, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='numero3',
            field=common.upper.UpperCharField(default=32, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='seccion',
            field=common.upper.UpperCharField(default='CALLE', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='telefono',
            field=common.upper.UpperCharField(default=2343434, max_length=20),
            preserve_default=False,
        ),
    ]
