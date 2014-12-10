# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0005_auto_20141208_1950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitud',
            old_name='productoss',
            new_name='productos',
        ),
    ]
