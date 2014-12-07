# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0010_remove_producto_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='foto',
            field=models.ImageField(null=True, upload_to=b'fotosproductos'),
            preserve_default=True,
        ),
    ]
