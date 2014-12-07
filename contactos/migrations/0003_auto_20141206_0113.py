# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0002_auto_20141116_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='apellido',
            field=common.upper.UpperCharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='cargo',
            field=common.upper.UpperCharField(max_length=25, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='celular',
            field=common.upper.UpperCharField(max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='extension',
            field=common.upper.UpperCharField(max_length=5, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='nombre',
            field=common.upper.UpperCharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='telefono',
            field=common.upper.UpperCharField(max_length=15, null=True, blank=True),
        ),
    ]
