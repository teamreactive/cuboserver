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
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
                ('ciudad', models.CharField(max_length=50, null=True, blank=True)),
                ('seccion', models.CharField(max_length=1, null=True, blank=True)),
                ('numero1', models.IntegerField(null=True)),
                ('numero2', models.IntegerField(null=True)),
                ('numero3', models.IntegerField(null=True)),
                ('descripcion', models.CharField(max_length=200, null=True, blank=True)),
                ('contactos', models.ManyToManyField(to='contactos.Contacto', db_table=b'lugarcontacto')),
                ('usuario', models.ForeignKey(related_name=b'Lugar.usuario', to='usuarios.Usuario', null=True)),
            ],
            options={
                'db_table': 'lugar',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='lugar',
            unique_together=set([('usuario', 'nombre')]),
        ),
    ]
