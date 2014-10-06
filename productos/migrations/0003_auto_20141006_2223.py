# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20141006_0231'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='producto',
            unique_together=set([('cliente', 'codigo_onu')]),
        ),
    ]
