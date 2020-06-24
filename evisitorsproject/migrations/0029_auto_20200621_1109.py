# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-21 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evisitorsproject', '0028_auto_20200621_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facerecognation',
            name='face',
        ),
        migrations.AddField(
            model_name='facerecognation',
            name='face_image',
            field=models.ImageField(null=True, upload_to='viewReport/'),
        ),
    ]
