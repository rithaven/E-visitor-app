# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-07-14 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evisitorsproject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanequipment',
            name='Id_number',
            field=models.CharField(max_length=21, null=True),
        ),
    ]