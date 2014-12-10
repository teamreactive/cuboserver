# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0004_remove_proveedor_cliente'),
        ('solicitudes', '0008_auto_20141210_0454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preciounitario', models.DecimalField(max_digits=12, decimal_places=2)),
                ('ivaa', models.DecimalField(max_digits=6, decimal_places=3)),
                ('tiempo', models.IntegerField()),
                ('referencia', common.upper.UpperCharField(max_length=25)),
                ('validez', common.upper.UpperCharField(max_length=25)),
                ('formapago', common.upper.UpperCharField(max_length=10)),
                ('producto', models.ForeignKey(related_name=b'Cotizacion.producto', on_delete=django.db.models.deletion.PROTECT, to='solicitudes.ProductoSolicitud')),
                ('proveedor', models.ForeignKey(related_name=b'Cotizacion.proveedor', on_delete=django.db.models.deletion.SET_NULL, to='proveedores.Proveedor', null=True)),
            ],
            options={
                'db_table': 'cotizacion',
            },
            bases=(models.Model,),
        ),
    ]
