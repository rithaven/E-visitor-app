# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-21 05:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evisitorsproject', '0022_auto_20200621_0504'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idscan',
            old_name='property',
            new_name='property_owner',
        ),
    ]
