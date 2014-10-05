# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('tiposdeequipos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('cantidad', models.IntegerField()),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
                ('tipo_de_equipo', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='tiposdeequipos.TipoDeEquipo', null=True)),
            ],
            options={
                'db_table': 'equipo',
            },
            bases=(models.Model,),
        ),
    ]
