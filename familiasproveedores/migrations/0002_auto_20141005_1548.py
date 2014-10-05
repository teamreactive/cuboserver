# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
        ('familiasproveedores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactosxfamiliaproveedor',
            name='contactos',
        ),
        migrations.RemoveField(
            model_name='contactosxfamiliaproveedor',
            name='familia_proveedor',
        ),
        migrations.DeleteModel(
            name='ContactosxFamiliaProveedor',
        ),
        migrations.AddField(
            model_name='familiaproveedor',
            name='contactos',
            field=models.ManyToManyField(to='contactos.Contacto', db_table=b'familiaproveedorxcontacto'),
            preserve_default=True,
        ),
    ]
