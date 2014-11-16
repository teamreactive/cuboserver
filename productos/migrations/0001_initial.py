# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
        ('clientes', '0001_initial'),
        ('familias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotoProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.ImageField(upload_to=b'fotoproducto')),
            ],
            options={
                'db_table': 'fotoproducto',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NombreProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'nombreproducto',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PrecioMesProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.CharField(max_length=2)),
                ('precio', models.FloatField()),
            ],
            options={
                'db_table': 'preciomesproducto',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('onu', models.CharField(max_length=25, null=True, blank=True)),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('referencia', models.CharField(max_length=25, null=True, blank=True)),
                ('marca', models.CharField(max_length=25)),
                ('servicio', models.BooleanField(default=False)),
                ('tiempopromedio', models.CharField(max_length=15, null=True, blank=True)),
                ('valido', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(related_name=b'Producto.cliente', to='clientes.Cliente')),
                ('contactonovende', models.ManyToManyField(related_name=b'Producto.contactonovende', db_table=b'productocontactonovende', to='contactos.Contacto')),
                ('contactovende', models.ManyToManyField(related_name=b'Producto.contactovende', db_table=b'productocontactovende', to='contactos.Contacto')),
                ('familia', models.ForeignKey(related_name=b'Producto.familia', to='familias.Familia', null=True)),
            ],
            options={
                'db_table': 'producto',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UnidadProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unidad', models.CharField(max_length=10)),
                ('talla', models.CharField(max_length=10, null=True, blank=True)),
                ('producto', models.ForeignKey(related_name=b'UnidadProducto.producto', to='productos.Producto')),
            ],
            options={
                'db_table': 'precioproducto',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='producto',
            unique_together=set([('cliente', 'onu')]),
        ),
        migrations.AddField(
            model_name='preciomesproducto',
            name='producto',
            field=models.ForeignKey(related_name=b'PrecioMesProducto.producto', to='productos.UnidadProducto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nombreproducto',
            name='producto',
            field=models.ForeignKey(related_name=b'NombreProducto.producto', to='productos.Producto'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='nombreproducto',
            unique_together=set([('producto', 'nombre')]),
        ),
        migrations.AddField(
            model_name='fotoproducto',
            name='producto',
            field=models.ForeignKey(related_name=b'FotoProducto.producto', to='productos.Producto'),
            preserve_default=True,
        ),
    ]
