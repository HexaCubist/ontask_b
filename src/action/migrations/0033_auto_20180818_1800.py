# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-18 08:30
from __future__ import unicode_literals

from django.db import migrations


def change_action_type(apps, schema_editor):
    """
    Traverse all actions to change personal_text by personalized_text

    :param apps:
    :param schema_editor:
    :return:
    """
    if schema_editor.connection.alias != 'default':
        return

    Action = apps.get_model('action', 'Action')
    for item in Action.objects.all():
        if item.action_type == 'json':
            item.action_type = 'personalized_json'
            item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0032_action_target_url'),
    ]

    operations = [
        migrations.RunPython(change_action_type),
    ]
