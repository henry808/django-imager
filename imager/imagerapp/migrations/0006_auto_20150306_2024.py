# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('imagerapp', '0005_auto_20150306_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='picture',
            field=models.ImageField(default=b'/static/images/default_profile_image.jpg', upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='user',
            field=models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
