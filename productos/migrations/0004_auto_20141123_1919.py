# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20141123_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotoproducto',
            name='producto',
            field=models.ForeignKey(related_name=b'fotos', to='productos.Producto'),
        ),
        migrations.AlterField(
            model_name='preciomesproducto',
            name='producto',
            field=models.ForeignKey(related_name=b'preciomes', to='productos.UnidadProducto'),
        ),
        migrations.AlterField(
            model_name='unidadproducto',
            name='producto',
            field=models.ForeignKey(related_name=b'unidades', to='productos.Producto'),
        ),
    ]
