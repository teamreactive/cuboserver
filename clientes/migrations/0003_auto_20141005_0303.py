# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_remove_cliente_lugar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='codigo_verificacion',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'logos', blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sigla',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
