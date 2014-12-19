# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20141206_0113'),
        ('solicitudes', '0008_auto_20141210_0454'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='cliente',
            field=models.ForeignKey(related_name=b'Solicitud.cliente', default=123456, to='clientes.Cliente'),
            preserve_default=False,
        ),
    ]
