# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0013_auto_20141217_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='usuario',
            field=common.upper.UpperCharField(default='a', unique=True, max_length=50),
            preserve_default=False,
        ),
    ]
