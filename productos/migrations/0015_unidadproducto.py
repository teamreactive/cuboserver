# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0014_auto_20141207_1917'),
    ]

    operations = [
        #migrations.DeleteModel("UnidadProducto"),
        migrations.CreateModel(
            name='UnidadProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unidad', models.CharField(max_length=10))
            ],
            options={
                'db_table': 'unidadproducto',
            },
            bases=(models.Model,),
        ),
    ]