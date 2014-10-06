# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio_unitario', models.DecimalField(max_digits=12, decimal_places=2)),
                ('iva', models.CharField(max_length=1, choices=[(b'1', b'16'), (b'2', b'1.6'), (b'3', b'20'), (b'4', b'0')])),
                ('referencia', models.CharField(max_length=25)),
                ('validez', models.CharField(max_length=25)),
                ('forma_de_pago', models.CharField(max_length=1, choices=[(b'1', b'anticipado'), (b'2', b'contado'), (b'3', b'dias')])),
                ('fecha_entrega', models.DateTimeField()),
                ('producto', models.ForeignKey(to='productos.Producto', on_delete=django.db.models.deletion.PROTECT)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='proveedores.Proveedor', null=True)),
            ],
            options={
                'db_table': 'cotizacion',
            },
            bases=(models.Model,),
        ),
    ]
