# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_auto_20141012_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='precioxproducto',
            name='precio_promedio',
        ),
    ]
