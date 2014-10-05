# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0004_auto_20141005_0303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lugar',
            old_name='user',
            new_name='usuario',
        ),
    ]
