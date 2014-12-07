# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='ciudad',
            field=common.upper.UpperCharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='descripcion',
            field=common.upper.UpperCharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='nombre',
            field=common.upper.UpperCharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='seccion',
            field=common.upper.UpperCharField(max_length=1, null=True, blank=True),
        ),
    ]
