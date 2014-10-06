# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25, null=True, blank=True)),
                ('direccion', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=100)),
                ('contactos', models.ManyToManyField(to='contactos.Contacto', db_table=b'lugarxcontactos')),
                ('usuario', models.ForeignKey(to='usuarios.Usuario', null=True)),
            ],
            options={
                'db_table': 'lugar',
            },
            bases=(models.Model,),
        ),
    ]
