# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20141006_2223'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='nombresxproducto',
            unique_together=set([('producto', 'nombre')]),
        ),
    ]
