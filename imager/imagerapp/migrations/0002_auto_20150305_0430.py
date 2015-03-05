# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('imagerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='birthday',
            field=models.DateField(default=datetime.date(2015, 3, 5)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='phone',
            field=models.IntegerField(max_length=11, blank=True),
            preserve_default=True,
        ),
    ]
