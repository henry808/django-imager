# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0003_auto_20150308_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date_published',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
