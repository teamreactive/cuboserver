# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDeEquipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
            ],
            options={
                'db_table': 'tipo_de_equipo',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='tipodeequipo',
            unique_together=set([('cliente', 'nombre')]),
        ),
    ]
