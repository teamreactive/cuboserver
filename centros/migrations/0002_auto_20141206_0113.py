# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('centros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centro',
            name='nombre',
            field=common.upper.UpperCharField(max_length=25),
        ),
    ]
