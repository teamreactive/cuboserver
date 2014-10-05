# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nit', models.CharField(max_length=25)),
                ('codigo_verificacion', models.CharField(max_length=25, null=True)),
                ('razon_social', models.CharField(max_length=25)),
                ('sigla', models.CharField(max_length=10, null=True)),
                ('logo', models.ImageField(null=True, upload_to=b'logos')),
                ('lugar', models.ForeignKey(related_name=b'Cliente', on_delete=django.db.models.deletion.PROTECT, to='lugares.Lugar', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
