# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagerapp', '0007_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagerprofile',
            name='followers',
            field=models.ForeignKey(to='imagerapp.ImagerProfile', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='picture',
            field=models.ImageField(default=b'/static/images\\default_profile_image.jpg', upload_to=b''),
            preserve_default=True,
        ),
    ]
