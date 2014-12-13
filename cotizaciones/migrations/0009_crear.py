# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import common.upper



class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0016_auto_20141207_2015'),
        ('proveedores', '0004_remove_proveedor_cliente'),
        ('cotizaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('producto', models.ForeignKey(related_name=b'Cotizacion.producto', to='productos.Producto')),
                ('preciounitario', models.DecimalField(max_digits=12, decimal_places=2)),
                ('iva', models.DecimalField(max_digits=6, decimal_places=3)),
                ('tiempo', models.IntegerField()),
                ('referencia', common.upper.UpperCharField(max_length=25)),
                ('validez', models.IntegerField()),
                ('formapago', common.upper.UpperCharField(max_length=20)),
                ('proveedor', models.ForeignKey(related_name=b'Cotizacion.proveedor', to='proveedores.Proveedor', null=True)),
            ],
            options={
                'db_table': 'cotizacion',
            },
            bases=(models.Model,),
        ),
    ]
