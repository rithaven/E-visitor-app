# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-21 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evisitorsproject', '0025_auto_20200621_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facerecognation',
            name='property_owner',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
