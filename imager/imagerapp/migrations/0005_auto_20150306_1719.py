# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagerapp', '0004_auto_20150306_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='phone',
            field=models.IntegerField(max_length=11, null=True, blank=True),
            preserve_default=True,
        ),
    ]
