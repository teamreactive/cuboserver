# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
        ('clientes', '0001_initial'),
        ('equipos', '0001_initial'),
        ('centrosdecostos', '0001_initial'),
        ('familiasproveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotosxProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NombresxProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PrecioxProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unidad', models.CharField(max_length=1)),
                ('talla', models.CharField(max_length=1)),
                ('precio_promedio', models.FloatField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_onu', models.CharField(max_length=25)),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.TextField(null=True)),
                ('referencia', models.CharField(max_length=25, null=True)),
                ('marca', models.CharField(max_length=25)),
                ('servicio', models.CharField(max_length=1, choices=[(b's', b'si'), (b'n', b'no')])),
                ('tiempo_promedio', models.CharField(max_length=15, null=True)),
                ('centro_de_costo', models.ForeignKey(to='centrosdecostos.CentroDeCosto', null=True)),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
                ('equipo', models.ForeignKey(to='equipos.Equipo', null=True)),
                ('familia_proveedor', models.ForeignKey(to='familiasproveedores.FamiliaProveedor', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductoxContactoQueNoVende',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contacto', models.ForeignKey(to='contactos.Contacto')),
                ('producto', models.ForeignKey(to='productos.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductoxContactoQueVende',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contacto', models.ForeignKey(to='contactos.Contacto')),
                ('producto', models.ForeignKey(to='productos.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='precioxproducto',
            name='producto',
            field=models.ForeignKey(to='productos.Producto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nombresxproducto',
            name='producto',
            field=models.ForeignKey(to='productos.Producto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fotosxproducto',
            name='producto',
            field=models.ForeignKey(to='productos.Producto'),
            preserve_default=True,
        ),
    ]
