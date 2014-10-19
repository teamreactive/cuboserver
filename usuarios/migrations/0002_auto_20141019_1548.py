# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='contrasena',
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=12345, max_length=112),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
    ]
