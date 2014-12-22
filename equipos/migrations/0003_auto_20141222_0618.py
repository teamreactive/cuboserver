# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0002_auto_20141206_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='equipo',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='equipo',
            name='tipoequipo',
            field=models.ForeignKey(related_name=b'Equipo.tipoequipo', to='tiposequipos.TipoEquipo'),
        ),
    ]
