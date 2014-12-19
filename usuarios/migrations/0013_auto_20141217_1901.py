# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_auto_20141217_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=common.upper.UpperCharField(unique=True, max_length=50),
        ),
    ]
