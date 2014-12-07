# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0011_producto_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unidad', models.CharField(max_length=10)),
                ('producto', models.ForeignKey(related_name='Producto.familia', to='Producto')),
            ],
            options={
                'db_table': 'unidadproducto',
            },
            bases=(models.Model,),
        )
    ]