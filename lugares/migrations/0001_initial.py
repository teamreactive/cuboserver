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
                ('seccion', models.CharField(max_length=1, choices=[(b'1', b'calle'), (b'2', b'carrera'), (b'3', b'transversal'), (b'4', b'avenida'), (b'5', b'diagonal')])),
                ('numero_seccion', models.CharField(max_length=5)),
                ('numero_1', models.CharField(max_length=5)),
                ('numero_2', models.CharField(max_length=5)),
                ('extra', models.CharField(max_length=100)),
                ('contactos', models.ManyToManyField(to='contactos.Contacto', db_table=b'lugarxcontactos')),
                ('usuario', models.ForeignKey(to='usuarios.Usuario', null=True)),
            ],
            options={
                'db_table': 'lugar',
            },
            bases=(models.Model,),
        ),
    ]
