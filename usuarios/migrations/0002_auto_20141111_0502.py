# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aprobadorcomprasalmacenista',
            name='almacenista',
            field=models.ForeignKey(related_name=b'AprobadorComprasAlmacenista.almacenista', to='usuarios.Usuario'),
        ),
        migrations.AlterField(
            model_name='aprobadorcomprasalmacenista',
            name='aprobador',
            field=models.ForeignKey(related_name=b'AprobadorComprasAlmacenista.aprobador', to='usuarios.Usuario'),
        ),
    ]
