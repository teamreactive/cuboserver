# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productoxcontactoquenovende',
            name='contacto',
        ),
        migrations.RemoveField(
            model_name='productoxcontactoquenovende',
            name='producto',
        ),
        migrations.DeleteModel(
            name='ProductoxContactoQueNoVende',
        ),
        migrations.RemoveField(
            model_name='productoxcontactoquevende',
            name='contacto',
        ),
        migrations.RemoveField(
            model_name='productoxcontactoquevende',
            name='producto',
        ),
        migrations.DeleteModel(
            name='ProductoxContactoQueVende',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='centro_de_costo',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='equipo',
        ),
        migrations.AddField(
            model_name='producto',
            name='contacto_novende',
            field=models.ManyToManyField(related_name=b'Producto.contacto_novende', db_table=b'productoxcontactoquenovende', to='contactos.Contacto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producto',
            name='contacto_vende',
            field=models.ManyToManyField(related_name=b'Producto.contacto_vende', db_table=b'productoxcontactoquevende', to='contactos.Contacto'),
            preserve_default=True,
        ),
    ]
