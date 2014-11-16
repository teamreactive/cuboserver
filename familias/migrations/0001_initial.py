# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('cliente', models.ForeignKey(related_name=b'Familia.cliente', to='clientes.Cliente')),
                ('contactos', models.ManyToManyField(related_name=b'Familia.contactos', db_table=b'familiacontacto', to='contactos.Contacto')),
            ],
            options={
                'db_table': 'familia',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='familia',
            unique_together=set([('nombre', 'cliente')]),
        ),
    ]
