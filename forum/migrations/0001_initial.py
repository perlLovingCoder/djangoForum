# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=600)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='thread',
            field=models.ForeignKey(to='forum.Thread'),
        ),
    ]
