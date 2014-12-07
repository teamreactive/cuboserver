# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0013_auto_20141207_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nombreproducto',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='unidadproducto',
            name='producto',
        ),
        migrations.AddField(
            model_name='producto',
            name='nombres',
            field=models.ManyToManyField(related_name=b'Producto.nombres', to='productos.NombreProducto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producto',
            name='unidades',
            field=models.ManyToManyField(related_name=b'Producto.unidades', to='productos.UnidadProducto'),
            preserve_default=True,
        ),
    ]
