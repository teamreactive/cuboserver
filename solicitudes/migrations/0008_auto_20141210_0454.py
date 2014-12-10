# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0007_auto_20141208_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='estado',
            field=common.upper.UpperCharField(default=b'0100', max_length=10),
        ),
    ]
