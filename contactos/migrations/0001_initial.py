# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('telefono', models.CharField(max_length=15, null=True, blank=True)),
                ('extension', models.CharField(max_length=5, null=True, blank=True)),
                ('celular', models.CharField(max_length=15, null=True, blank=True)),
                ('email', models.EmailField(max_length=25, null=True, blank=True)),
                ('cargo', models.CharField(max_length=25, null=True, blank=True)),
                ('perfil', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'contacto',
            },
            bases=(models.Model,),
        ),
    ]
