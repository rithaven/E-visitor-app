# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-21 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evisitorsproject', '0023_auto_20200621_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idscan',
            name='property_owner',
            field=models.CharField(choices=[('A visitor', ((11, 'v_Laptop'), (12, 'v_tablet'), (13, 'v_Desktop machine'))), ('Instutition', ((11, 'inst_Laptop'), (12, 'inst_tablet'), (13, 'inst_Desktop machine'))), ('current instutition', ((11, 'current_Laptop'), (12, 'current_tablet'), (13, 'current_Desktop machine')))], max_length=300, null=True),
        ),
    ]
