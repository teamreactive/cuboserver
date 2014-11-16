# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20141110_2247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='clientepk',
            new_name='id',
        ),
    ]
