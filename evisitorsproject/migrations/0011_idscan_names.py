# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-08-11 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evisitorsproject', '0010_auto_20200810_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='idscan',
            name='Names',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
