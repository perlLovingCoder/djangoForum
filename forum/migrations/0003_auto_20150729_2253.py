# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_comment_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='createdAt',
            field=models.DateField(default=datetime.datetime(2015, 7, 30, 2, 52, 36, 984000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='updatedAt',
            field=models.DateField(default=datetime.datetime(2015, 7, 30, 2, 52, 43, 333000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thread',
            name='createdAt',
            field=models.DateField(default=datetime.datetime(2015, 7, 30, 2, 52, 57, 75000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thread',
            name='updatedAt',
            field=models.DateField(default=datetime.datetime(2015, 7, 30, 2, 53, 2, 436000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
