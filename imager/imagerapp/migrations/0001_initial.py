# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'')),
                ('birthday', models.DateField()),
                ('phone', models.IntegerField(max_length=11)),
                ('pic_privacy', models.CharField(default=b'PR', max_length=2, choices=[(b'PR', b'Private'), (b'PU', b'Public')])),
                ('birthday_privacy', models.CharField(default=b'PR', max_length=2, choices=[(b'PR', b'Private'), (b'PU', b'Public')])),
                ('phone_privacy', models.CharField(default=b'PR', max_length=2, choices=[(b'PR', b'Private'), (b'PU', b'Public')])),
                ('name_privacy', models.CharField(default=b'PR', max_length=2, choices=[(b'PR', b'Private'), (b'PU', b'Public')])),
                ('email_privacy', models.CharField(default=b'PR', max_length=2, choices=[(b'PR', b'Private'), (b'PU', b'Public')])),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
