# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='valido',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fotosxproducto',
            name='foto',
            field=models.ImageField(upload_to=b'imagenes_productos'),
        ),
        migrations.AlterField(
            model_name='precioxproducto',
            name='talla',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='precioxproducto',
            name='unidad',
            field=models.CharField(max_length=10),
        ),
    ]
