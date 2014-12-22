# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiposequipos', '0002_auto_20141206_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipoequipo',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='tipoequipo',
            name='numero',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
