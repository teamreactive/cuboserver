# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0009_auto_20141207_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='foto',
        ),
    ]
