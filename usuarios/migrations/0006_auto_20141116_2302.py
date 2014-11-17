# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_auto_20141116_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cliente',
            field=models.ForeignKey(related_name=b'Usuario.cliente', blank=True, to='clientes.Cliente', null=True),
        ),
    ]
