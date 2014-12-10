# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from common import upper

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    	('lugares', '0001_initial'),
        ('clientes', '0006_auto_20141206_0113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cliente', models.ForeignKey(related_name=b'Lugar.cliente', to='clientes.Cliente')),
                ('nombre', upper.UpperCharField(max_length=100)),
                ('ciudad', upper.UpperCharField(max_length=50)),
                ('seccion', upper.UpperCharField(max_length=20)),
                ('numero1', upper.UpperCharField(max_length=5)),
                ('numero2', upper.UpperCharField(max_length=5)),
                ('numero3', upper.UpperCharField(max_length=5)),
                ('telefono', upper.UpperCharField(max_length=20)),
            ],
            options={
                'db_table': 'lugar',
            },
            bases=(models.Model,),
        ),
    ]