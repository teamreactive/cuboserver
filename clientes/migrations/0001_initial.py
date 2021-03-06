# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nit', models.CharField(unique=True, max_length=25)),
                ('verificacion', models.CharField(max_length=25, unique=True, null=True, blank=True)),
                ('razon', models.CharField(unique=True, max_length=25)),
                ('sigla', models.CharField(max_length=10, null=True, blank=True)),
                ('logo', models.ImageField(null=True, upload_to=b'logos', blank=True)),
            ],
            options={
                'db_table': 'cliente',
            },
            bases=(models.Model,),
        ),
    ]
