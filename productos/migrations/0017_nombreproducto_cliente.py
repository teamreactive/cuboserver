# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20141206_0113'),
        ('productos', '0016_auto_20141207_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='nombreproducto',
            name='cliente',
            field=models.ForeignKey(related_name=b'NombreProducto.cliente', default=123456, to='clientes.Cliente'),
            preserve_default=False,
        ),
    ]
