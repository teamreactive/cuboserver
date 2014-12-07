# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0003_auto_20141206_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='email',
            field=common.upper.UpperCharField(max_length=320, null=True, blank=True),
        ),
    ]
