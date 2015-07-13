# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugs', '0002_auto_20150712_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='assignee',
            field=models.ForeignKey(related_name='assignee', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='bug',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'created_at'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='owner',
            field=models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
