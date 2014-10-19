# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0003_auto_20141019_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='numero_1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='numero_2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='numero_3',
            field=models.IntegerField(null=True),
        ),
    ]
