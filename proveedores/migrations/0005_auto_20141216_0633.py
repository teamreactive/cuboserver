# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20141206_0113'),
        ('proveedores', '0004_remove_proveedor_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='cliente',
            field=models.ForeignKey(related_name=b'Proveedor.cliente', default=123456, to='clientes.Cliente'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='logo',
            field=models.ImageField(upload_to=b'logos/proovedores'),
        ),
    ]
