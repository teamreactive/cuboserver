# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_auto_20141206_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='calificacion',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='contactos',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='cotizacion',
        ),
        migrations.AlterUniqueTogether(
            name='proveedor',
            unique_together=None,
        ),
    ]
