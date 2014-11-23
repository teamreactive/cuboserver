# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20141116_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cliente',
            field=models.OneToOneField(to='clientes.Cliente'),
        ),
    ]
