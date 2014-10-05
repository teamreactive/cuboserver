# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
        ('familiasproveedores', '0002_auto_20141005_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactosxFamiliaProveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contactos', models.ForeignKey(to='contactos.Contacto')),
                ('familia_proveedor', models.ForeignKey(to='familiasproveedores.FamiliaProveedor')),
            ],
            options={
                'db_table': 'contactos_por_familia_proveedor',
            },
            bases=(models.Model,),
        ),
    ]
