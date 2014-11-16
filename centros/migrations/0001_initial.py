# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('cliente', models.ForeignKey(related_name=b'Centro.cliente', to='clientes.Cliente')),
            ],
            options={
                'db_table': 'centro',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='centro',
            unique_together=set([('nombre', 'cliente')]),
        ),
    ]
