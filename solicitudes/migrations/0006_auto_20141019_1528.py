# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0005_auto_20141019_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoxsolicitud',
            name='linea',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='productoxsolicitud',
            name='solicitud',
            field=models.ForeignKey(to='solicitudes.Solicitud'),
        ),
        migrations.AddField(
            model_name='productoxsolicitud',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=None, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
