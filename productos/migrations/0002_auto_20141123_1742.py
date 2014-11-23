# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='familia',
            field=models.ForeignKey(related_name=b'Producto.familia', to='familias.Familia'),
        ),
    ]
