# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_node_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='state',
            field=models.SmallIntegerField(default=0, choices=[(0, b'undefined'), (1, b'alive'), (2, b'dead')]),
            preserve_default=True,
        ),
    ]
