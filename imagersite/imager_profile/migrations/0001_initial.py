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
                ('fav_camera', models.CharField(max_length=256)),
                ('address', models.TextField()),
                ('url', models.URLField()),
                ('photo_type', models.CharField(default=b'N', max_length=1, choices=[(b'N', b'Nature Photography'), (b'P', b'Paranormal Photography'), (b'A', b'Aerial Photography'), (b'B', b'Black and White Photography'), (b'F', b'Forensic Photography')])),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
