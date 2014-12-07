# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0012_unidadproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidadproducto',
            name='producto',
            field=models.ForeignKey(related_name=b'UnidadProducto.producto', to='productos.Producto'),
        ),
        migrations.AlterField(
            model_name='unidadproducto',
            name='unidad',
            field=common.upper.UpperCharField(max_length=10),
        ),
    ]
