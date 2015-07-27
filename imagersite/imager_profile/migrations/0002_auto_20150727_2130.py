# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='fav_camera',
            field=models.CharField(max_length=256, blank=True),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
