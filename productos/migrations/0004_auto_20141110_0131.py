# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0002_auto_20141110_0131'),
        ('productos', '0003_precioproductoxmes'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadXProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unidad', models.CharField(max_length=10)),
                ('talla', models.CharField(max_length=10, null=True, blank=True)),
                ('producto', models.ForeignKey(to='productos.Producto')),
            ],
            options={
                'db_table': 'precio_producto',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='precioxproducto',
            name='producto',
        ),
        migrations.DeleteModel(
            name='PrecioxProducto',
        ),
        migrations.AlterField(
            model_name='precioproductoxmes',
            name='mes',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='precioproductoxmes',
            name='producto',
            field=models.ForeignKey(to='productos.UnidadXProducto'),
        ),
    ]
