# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 05:57
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0016_auto_20180409_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='categories',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list, null=True, verbose_name='Comma separated list of values allowed in this column'),
        ),
    ]
