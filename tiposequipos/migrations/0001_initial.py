# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEquipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('cliente', models.ForeignKey(related_name=b'TipoEquipo.cliente', to='clientes.Cliente')),
            ],
            options={
                'db_table': 'tipoequipo',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='tipoequipo',
            unique_together=set([('cliente', 'nombre')]),
        ),
    ]
