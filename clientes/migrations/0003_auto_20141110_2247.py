# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20141110_2244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='id',
            new_name='clientepk',
        ),
    ]
