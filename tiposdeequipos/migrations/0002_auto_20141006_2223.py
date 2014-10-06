# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiposdeequipos', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tipodeequipo',
            unique_together=set([('cliente', 'nombre')]),
        ),
    ]
