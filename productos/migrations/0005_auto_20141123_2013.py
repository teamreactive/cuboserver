# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_auto_20141123_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cliente',
            field=models.ForeignKey(related_name=b'productos', to='clientes.Cliente'),
        ),
    ]
