# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20141206_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='ciudad',
            field=common.upper.UpperCharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='numero1',
            field=common.upper.UpperCharField(max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='numero2',
            field=common.upper.UpperCharField(max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='numero3',
            field=common.upper.UpperCharField(max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='seccion',
            field=common.upper.UpperCharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='sector',
            field=common.upper.UpperCharField(max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=common.upper.UpperCharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
