# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0003_auto_20141209_0106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='cliente',
        ),
    ]
