# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='ip',
            field=models.IPAddressField(default=b'0.0.0.0'),
            preserve_default=True,
        ),
    ]
