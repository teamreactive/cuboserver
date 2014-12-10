# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0002_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='nombre',
            field=common.upper.UpperCharField(max_length=100, null=True),
        ),
    ]
