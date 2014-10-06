# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lugar',
            old_name='extra',
            new_name='descripcion',
        ),
        migrations.RemoveField(
            model_name='lugar',
            name='numero_1',
        ),
        migrations.RemoveField(
            model_name='lugar',
            name='numero_2',
        ),
        migrations.RemoveField(
            model_name='lugar',
            name='numero_seccion',
        ),
        migrations.RemoveField(
            model_name='lugar',
            name='seccion',
        ),
        migrations.AddField(
            model_name='lugar',
            name='direccion',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
    ]
