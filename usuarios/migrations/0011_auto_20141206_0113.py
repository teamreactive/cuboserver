# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_auto_20141123_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='activo',
            field=common.upper.UpperCharField(max_length=1, choices=[(b'0', b'no'), (b'1', b'si')]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=common.upper.UpperCharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=common.upper.UpperCharField(max_length=130),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=common.upper.UpperCharField(max_length=1, choices=[(b'1', b'administrador_general'), (b'2', b'administrador_cliente'), (b'3', b'solicitante'), (b'4', b'codificador'), (b'5', b'aprobador_solicitudes'), (b'6', b'comprador'), (b'7', b'aprobador_compra'), (b'8', b'almacenista')]),
        ),
    ]
