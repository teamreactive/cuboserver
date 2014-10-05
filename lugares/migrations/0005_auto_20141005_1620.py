# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
        ('lugares', '0004_auto_20141005_0303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lugarxcontacto',
            name='contacto',
        ),
        migrations.RemoveField(
            model_name='lugarxcontacto',
            name='lugar',
        ),
        migrations.DeleteModel(
            name='LugarxContacto',
        ),
        migrations.AddField(
            model_name='lugar',
            name='contactos',
            field=models.ManyToManyField(to='contactos.Contacto', db_table=b'lugarxcontactos'),
            preserve_default=True,
        ),
    ]
