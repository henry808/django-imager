# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagerapp', '0010_auto_20150306_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='following',
            field=models.ManyToManyField(related_name='followers', null=True, to='imagerapp.ImagerProfile'),
            preserve_default=True,
        ),
    ]
