# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_remove_cliente_lugar'),
        ('lugares', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lugar',
            name='cliente',
            field=models.ForeignKey(to='clientes.Cliente', null=True),
            preserve_default=True,
        ),
    ]
