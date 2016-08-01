# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_node_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='state',
            field=models.SmallIntegerField(default=0, choices=[(b'undefined', 0), (b'alive', 1), (b'dead', 2)]),
            preserve_default=True,
        ),
    ]
