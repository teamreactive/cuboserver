# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0001_initial'),
        ('contactos', '0001_initial'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactosxProveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contacto', models.ForeignKey(related_name=b'CxP.contacto', to='contactos.Contacto')),
            ],
            options={
                'db_table': 'contacto_por_proveedor',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('razon_social', models.CharField(max_length=25)),
                ('sigla', models.CharField(max_length=10)),
                ('nit', models.CharField(max_length=25)),
                ('numero_verificacion', models.CharField(max_length=25)),
                ('logo', models.FileField(upload_to=b'logos/proovedores')),
                ('calificacion', models.IntegerField()),
                ('cotizacion_defecto', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(related_name=b'Proveedor.cliente', to='clientes.Cliente')),
                ('lugar', models.ForeignKey(related_name=b'Proveedor.lugar', to='lugares.Lugar')),
            ],
            options={
                'db_table': 'proveedor',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='proveedor',
            unique_together=set([('cliente', 'nit')]),
        ),
        migrations.AddField(
            model_name='contactosxproveedor',
            name='proveedor',
            field=models.ForeignKey(related_name=b'CxP.proveedor', to='proveedores.Proveedor'),
            preserve_default=True,
        ),
    ]
