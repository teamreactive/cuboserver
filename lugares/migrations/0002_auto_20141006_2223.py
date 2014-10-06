# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='descripcion',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='lugar',
            unique_together=set([('usuario', 'direccion'), ('usuario', 'nombre')]),
        ),
    ]
