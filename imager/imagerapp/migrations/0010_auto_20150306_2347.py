# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagerapp', '0009_auto_20150306_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagerprofile',
            name='followers',
        ),
        migrations.AddField(
            model_name='imagerprofile',
            name='following',
            field=models.ManyToManyField(related_name='following_rel_+', null=True, to='imagerapp.ImagerProfile'),
            preserve_default=True,
        ),
    ]
