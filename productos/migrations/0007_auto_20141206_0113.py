# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_auto_20141123_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nombreproducto',
            name='nombre',
            field=common.upper.UpperCharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='preciomesproducto',
            name='mes',
            field=common.upper.UpperCharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=common.upper.UpperCharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=common.upper.UpperCharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='producto',
            name='onu',
            field=common.upper.UpperCharField(max_length=25, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='referencia',
            field=common.upper.UpperCharField(max_length=25, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='unidadproducto',
            name='talla',
            field=common.upper.UpperCharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='unidadproducto',
            name='unidad',
            field=common.upper.UpperCharField(max_length=10),
        ),
    ]
