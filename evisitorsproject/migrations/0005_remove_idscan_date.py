# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-18 06:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evisitorsproject', '0004_remove_idscan_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idscan',
            name='date',
        ),
    ]
