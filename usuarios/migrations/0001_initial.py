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
            name='AprobadorCompraxAlmacenista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'aprobador_compras_por_almacenista',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AprobadorSolicitudesxComprador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'aprobador_solicitudes_por_comprador',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AprobadorSolicitudesxSolicitante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'aprobador_solicitudes_por_solicitante',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompradorxAprobadorCompras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'comprador_por_aprobador_compras',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConsolidadorxSolicitante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'consolidador_por_solicitante',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SolicitantexCodificador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'solicitante_por_codificador',
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
            model_name='solicitantexcodificador',
            name='codificador',
            field=models.ForeignKey(related_name=b'SxC.codificador', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='solicitantexcodificador',
            name='solicitante',
            field=models.ForeignKey(related_name=b'SxC.solicitante', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='consolidadorxsolicitante',
            name='consolidador',
            field=models.ForeignKey(related_name=b'CxS.consolidador', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='consolidadorxsolicitante',
            name='solicitante',
            field=models.ForeignKey(related_name=b'CxS.solicitante', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compradorxaprobadorcompras',
            name='aprobador',
            field=models.ForeignKey(related_name=b'CxAC.aprobador', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compradorxaprobadorcompras',
            name='comprador',
            field=models.ForeignKey(related_name=b'CxAC.comprador', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aprobadorsolicitudesxsolicitante',
            name='aprobador',
            field=models.ForeignKey(related_name=b'ASxS.aprobador', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aprobadorsolicitudesxsolicitante',
            name='solicitante',
            field=models.ForeignKey(related_name=b'ASxS.solicitante', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aprobadorsolicitudesxcomprador',
            name='aprobador',
            field=models.ForeignKey(related_name=b'ASxC.aprobador', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aprobadorsolicitudesxcomprador',
            name='comprador',
            field=models.ForeignKey(related_name=b'ASxC.comprador', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aprobadorcompraxalmacenista',
            name='almacenista',
            field=models.ForeignKey(related_name=b'ACxA.almacenista', to='usuarios.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aprobadorcompraxalmacenista',
            name='aprobador',
            field=models.ForeignKey(related_name=b'ACxA.aprobador', to='usuarios.Usuario'),
            preserve_default=True,
        ),
    ]
