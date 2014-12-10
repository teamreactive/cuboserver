# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0003_auto_20141206_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='proyecto',
        ),
        migrations.AddField(
            model_name='productosolicitud',
            name='unidad',
            field=common.upper.UpperCharField(default='KG', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='estado',
            field=common.upper.UpperCharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='fechacreacion',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterUniqueTogether(
            name='productosolicitud',
            unique_together=None,
        ),
    ]
