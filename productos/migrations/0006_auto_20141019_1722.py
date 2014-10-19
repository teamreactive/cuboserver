# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_remove_precioxproducto_precio_promedio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precioxproducto',
            name='talla',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
