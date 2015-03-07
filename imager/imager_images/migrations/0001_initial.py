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
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_uploaded', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_published', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
                ('published', models.CharField(default=b'PR', max_length=2, choices=[(b'PR', b'Private'), (b'SH', b'Shard'), (b'PU', b'Public')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'')),
                ('date_uploaded', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_published', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
                ('published', models.CharField(default=b'PR', max_length=2, choices=[(b'PR', b'Private'), (b'SH', b'Shard'), (b'PU', b'Public')])),
                ('user', models.ForeignKey(related_name='photo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(related_name='albums', null=True, to='imager_images.Photo', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(related_name='albums', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
