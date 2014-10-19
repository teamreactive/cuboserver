    # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotosxproducto',
            name='foto',
            field=models.ImageField(upload_to=b'imagenes_productos'),
        ),
        migrations.AlterField(
            model_name='precioxproducto',
            name='talla',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='precioxproducto',
            name='unidad',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='nombresxproducto',
            unique_together=set([('producto', 'nombre')]),
        ),
        migrations.AlterUniqueTogether(
            name='producto',
            unique_together=set([('cliente', 'codigo_onu')]),
        ),
    ]   
