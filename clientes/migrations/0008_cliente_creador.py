# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0015_auto_20141222_0423'),
        ('clientes', '0007_auto_20141221_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='creador',
            field=models.ForeignKey(related_name=b'Cliente.creador', to='usuarios.Usuario', null=True),
            preserve_default=True,
        ),
    ]
