# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0004_auto_20141112_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='state',
            field=models.SmallIntegerField(default=0, choices=[(0, b'alive'), (1, b'dead'), (2, b'undefined')]),
            preserve_default=True,
        ),
    ]
