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
            name='AprobadorComprasAlmacenista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'aprobadorcomprasalmacenista',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AprobadorSolicitudesComprador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'aprobadorsolicitudescomprador',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AprobadorSolicitudesSolicitante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'aprobadorsolicitudessolicitante',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompradorAprobadorCompras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'compradoraprobadorcompras',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConsolidadorSolicitante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'consolidadorsolicitante',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SolicitanteCodificador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'solicitantecodificador',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=112)),
                ('tipo', models.CharField(max_length=1, choices=[(b'1', b'administrador_general'), (b'2', b'administrador_cliente'), (b'3', b'solicitante'), (b'4', b'codificador'), (b'5', b'aprobador_solicitudes'), (b'6', b'comprador'), (b'7', b'aprobador_compra'), (b'8', b'almacenista')])),
                ('activo', models.CharField(max_length=1, choices=[(b'0', b'no'), (b'1', b'si')])),
                ('cliente', models.ForeignKey(related_name=b'Usuario.cliente', to='clientes.Cliente', null=True)),
                ('contacto', models.ForeignKey(related_name=b'Usuario.contacto', to='contactos.Contacto')),
            ],
            options={
                'db_table': 'usuario',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='solicitantecodificador',
            name='codificador',
            field=models.ForeignKey(related_name=b'SolicitanteCodificador.codificador', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='solicitantecodificador',
            name='solicitante',
            field=models.ForeignKey(related_name=b'SolicitanteCodificador.solicitante', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='consolidadorsolicitante',
            name='consolidador',
            field=models.ForeignKey(related_name=b'ConsolidadorSolicitante.consolidador', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='consolidadorsolicitante',
            name='solicitante',
            field=models.ForeignKey(related_name=b'ConsolidadorSolicitante.solicitante', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compradoraprobadorcompras',
            name='aprobador',
            field=models.ForeignKey(related_name=b'CompradorAprobadorCompras.aprobador', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compradoraprobadorcompras',
            name='comprador',
            field=models.ForeignKey(related_name=b'CompradorAprobadorCompras.comprador', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aprobadorsolicitudessolicitante',
            name='aprobador',
            field=models.ForeignKey(related_name=b'AprobadorSolicitudesSolicitante.aprobador', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aprobadorsolicitudessolicitante',
            name='solicitante',
            field=models.ForeignKey(related_name=b'AprobadorSolicitudesSolicitante.solicitante', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aprobadorsolicitudescomprador',
            name='aprobador',
            field=models.ForeignKey(related_name=b'AprobadorSolicitudesComprador.aprobador', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aprobadorsolicitudescomprador',
            name='comprador',
            field=models.ForeignKey(related_name=b'AprobadorSolicitudesComprador.comprador', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aprobadorcomprasalmacenista',
            name='almacenista',
            field=models.ForeignKey(related_name=b'AprobadorCompraAlmacenista.almacenista', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aprobadorcomprasalmacenista',
            name='aprobador',
            field=models.ForeignKey(related_name=b'AprobadorCompraAlmacenista.aprobador', to='usuarios.Usuario'),
            preserve_default=True,
        ),
    ]
