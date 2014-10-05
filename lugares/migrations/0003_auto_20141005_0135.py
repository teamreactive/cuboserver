# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('lugares', '0002_lugar_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lugar',
            name='cliente',
        ),
        migrations.AddField(
            model_name='lugar',
            name='user',
            field=models.ForeignKey(to='usuarios.Usuario', null=True),
            preserve_default=True,
        ),
    ]
