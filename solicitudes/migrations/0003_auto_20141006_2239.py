# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0002_auto_20141006_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='fecha_requerida',
            field=models.DateField(),
        ),
    ]
