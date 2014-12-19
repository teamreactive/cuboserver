# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familias', '0002_auto_20141206_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familia',
            name='contactos',
        ),
    ]
