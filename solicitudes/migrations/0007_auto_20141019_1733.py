# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0006_auto_20141019_1528'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productoxsolicitud',
            unique_together=set([('linea', 'solicitud')]),
        ),
    ]
