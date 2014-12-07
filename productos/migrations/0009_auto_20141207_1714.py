# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import common.upper


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0008_auto_20141206_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fotoproducto',
            name='producto',
        ),
        migrations.DeleteModel(
            name='FotoProducto',
        ),
        migrations.RemoveField(
            model_name='preciomesproducto',
            name='producto',
        ),
        migrations.DeleteModel(
            name='PrecioMesProducto',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='valido',
            new_name='activo',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='contactonovende',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='contactovende',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='servicio',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='tiempopromedio',
        ),
        migrations.RemoveField(
            model_name='unidadproducto',
            name='talla',
        ),
        migrations.AddField(
            model_name='producto',
            name='foto',
            field=models.ImageField(null=True, upload_to=b'fotosproductos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producto',
            name='talla',
            field=common.upper.UpperCharField(max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=common.upper.UpperCharField(default='BIEN', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nombreproducto',
            name='nombre',
            field=common.upper.UpperCharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='nombreproducto',
            name='producto',
            field=models.ForeignKey(related_name=b'NombreProducto.producto', to='productos.Producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='cliente',
            field=models.ForeignKey(related_name=b'Producto.cliente', to='clientes.Cliente'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=common.upper.UpperCharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='producto',
            name='onu',
            field=common.upper.UpperCharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='referencia',
            field=common.upper.UpperCharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='unidadproducto',
            name='producto',
            field=models.ForeignKey(related_name=b'UnidadProducto.producto', to='productos.Producto'),
        ),
        migrations.AlterUniqueTogether(
            name='nombreproducto',
            unique_together=None,
        ),
        migrations.AlterUniqueTogether(
            name='producto',
            unique_together=None,
        ),
    ]
