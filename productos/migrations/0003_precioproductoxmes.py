# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20141019_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrecioProductoXMes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.CharField(max_length=3)),
                ('precio', models.FloatField()),
                ('producto', models.ForeignKey(to='productos.Producto')),
            ],
            options={
                'db_table': 'precio_mes',
            },
            bases=(models.Model,),
        ),
    ]
