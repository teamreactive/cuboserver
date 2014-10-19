# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamiliaProveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
                ('contactos', models.ManyToManyField(to='contactos.Contacto', db_table=b'familiaproveedorxcontacto')),
            ],
            options={
                'db_table': 'familia_proveedor',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='familiaproveedor',
            unique_together=set([('nombre', 'cliente')]),
        ),
    ]
