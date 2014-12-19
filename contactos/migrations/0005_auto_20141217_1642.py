# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20141206_0113'),
        ('familias', '0003_remove_familia_contactos'),
        ('proveedores', '0005_auto_20141216_0633'),
        ('contactos', '0004_auto_20141206_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='cliente',
            field=models.ForeignKey(related_name=b'Contacto.cliente', default=123456, to='clientes.Cliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacto',
            name='familia',
            field=models.ForeignKey(related_name=b'Contacto.familia', default=1, to='familias.Familia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacto',
            name='proveedor',
            field=models.ForeignKey(related_name=b'Contacto.proveedor', default=1, to='proveedores.Proveedor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contacto',
            name='apellido',
            field=common.upper.UpperCharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='nombre',
            field=common.upper.UpperCharField(max_length=50),
        ),
    ]
