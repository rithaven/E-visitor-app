# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-08-30 19:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evisitorsproject', '0002_visitorinfo_firstname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idscan',
            name='Names',
        ),
    ]