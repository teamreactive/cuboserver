# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='codigo_verificacion',
            field=models.CharField(max_length=25, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nit',
            field=models.CharField(unique=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='razon_social',
            field=models.CharField(unique=True, max_length=25),
        ),
    ]
