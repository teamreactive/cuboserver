# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('descripcion', models.TextField()),
                ('usuario', models.ForeignKey(related_name=b'Historial.usuario', to='usuarios.Usuario')),
            ],
            options={
                'db_table': 'historial',
            },
            bases=(models.Model,),
        ),
    ]
