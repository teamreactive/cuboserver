# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0004_auto_20141019_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productoxsolicitud',
            name='id',
        ),
        migrations.AddField(
            model_name='productoxsolicitud',
            name='linea',
            field=models.IntegerField(default=None, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productoxsolicitud',
            name='solicitud',
            field=models.ForeignKey(to='solicitudes.Solicitud', primary_key=True),
        ),
    ]
