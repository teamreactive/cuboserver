# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0011_auto_20141206_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='contacto',
        ),
        migrations.AddField(
            model_name='usuario',
            name='apellido',
            field=common.upper.UpperCharField(default='FLOREZ', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='celular',
            field=common.upper.UpperCharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=common.upper.UpperCharField(default='PIPEFLOREZ@DA.COM', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='extension',
            field=common.upper.UpperCharField(max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono',
            field=common.upper.UpperCharField(default=1234566, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='activo',
            field=common.upper.UpperCharField(default=b'SI', max_length=2),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cliente',
            field=models.ForeignKey(to='clientes.Cliente'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=common.upper.UpperCharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=common.upper.UpperCharField(max_length=25),
        ),
    ]
