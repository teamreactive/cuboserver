# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0005_auto_20141217_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='familia',
            field=models.ForeignKey(related_name=b'Contacto.familia', to='familias.Familia', null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='proveedor',
            field=models.ForeignKey(related_name=b'Contacto.proveedor', to='proveedores.Proveedor', null=True),
        ),
    ]
