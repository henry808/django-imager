# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagerapp', '0002_auto_20150305_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagerprofile',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
