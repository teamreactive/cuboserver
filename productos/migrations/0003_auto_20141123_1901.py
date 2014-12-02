# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20141123_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nombreproducto',
            name='producto',
            field=models.ForeignKey(related_name=b'nombres', to='productos.Producto'),
        ),
    ]
