# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0003_auto_20141005_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='nombre',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
    ]
