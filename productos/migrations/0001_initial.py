# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
        ('clientes', '0001_initial'),
        ('familiasproveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotosxProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.ImageField(upload_to=b'imagenes_productos')),
            ],
            options={
                'db_table': 'fotos_por_producto',
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
                'db_table': 'nombre_por_producto',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PrecioxProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unidad', models.CharField(max_length=10)),
                ('talla', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'db_table': 'precio_producto',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_onu', models.CharField(max_length=25)),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('referencia', models.CharField(max_length=25, null=True, blank=True)),
                ('marca', models.CharField(max_length=25)),
                ('servicio', models.BooleanField(default=False)),
                ('tiempo_promedio', models.CharField(max_length=15, null=True, blank=True)),
                ('valido', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
                ('contacto_novende', models.ManyToManyField(related_name=b'Producto.contacto_novende', db_table=b'productoxcontactoquenovende', to='contactos.Contacto')),
                ('contacto_vende', models.ManyToManyField(related_name=b'Producto.contacto_vende', db_table=b'productoxcontactoquevende', to='contactos.Contacto')),
                ('familia_proveedor', models.ForeignKey(to='familiasproveedores.FamiliaProveedor', null=True)),
            ],
            options={
                'db_table': 'producto',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='producto',
            unique_together=set([('cliente', 'codigo_onu')]),
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
        migrations.AlterUniqueTogether(
            name='nombresxproducto',
            unique_together=set([('producto', 'nombre')]),
        ),
        migrations.AddField(
            model_name='fotosxproducto',
            name='producto',
            field=models.ForeignKey(to='productos.Producto'),
            preserve_default=True,
        ),
    ]
