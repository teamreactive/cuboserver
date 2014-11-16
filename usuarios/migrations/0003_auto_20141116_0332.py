# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20141111_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='contacto',
            field=models.ForeignKey(related_name=b'Usuario.contacto', to='contactos.Contacto', null=True),
        ),
    ]
