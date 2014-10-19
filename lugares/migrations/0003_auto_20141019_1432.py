# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0002_auto_20141006_2223'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lugar',
            unique_together=set([('usuario', 'nombre')]),
        ),
        migrations.RemoveField(
            model_name='lugar',
            name='direccion',
        ),
        migrations.AddField(
            model_name='lugar',
            name='ciudad',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lugar',
            name='numero_1',
            field=models.IntegerField(null=True,default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lugar',
            name='numero_2',
            field=models.IntegerField(null=True,default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lugar',
            name='numero_3',
            field=models.IntegerField(null=True,default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lugar',
            name='seccion',
            field=models.CharField(max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lugar',
            name='contactos',
            field=models.ManyToManyField(to=b'contactos.Contacto', db_table=b'lugaresxcontactos'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='descripcion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='nombre',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
