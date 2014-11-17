# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20141116_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cliente',
            field=models.OneToOneField(null=True, blank=True, to='clientes.Cliente'),
        ),
    ]
