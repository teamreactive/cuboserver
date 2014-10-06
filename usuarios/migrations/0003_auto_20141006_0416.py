# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20141006_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='contrasena',
            field=models.CharField(max_length=255),
        ),
    ]
