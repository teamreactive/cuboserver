# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('tiposequipos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoequipo',
            name='nombre',
            field=common.upper.UpperCharField(max_length=25),
        ),
    ]
