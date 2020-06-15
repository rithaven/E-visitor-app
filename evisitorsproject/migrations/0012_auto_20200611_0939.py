# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-11 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evisitorsproject', '0011_auto_20200603_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facerecognation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Idnumber', models.CharField(max_length=30, null=True)),
                ('FirstName', models.CharField(max_length=30, null=True)),
                ('LastName', models.CharField(max_length=30, null=True)),
                ('EntryTime', models.DateField(null=True)),
                ('ExitTime', models.DateField(null=True)),
                ('propertycode', models.CharField(max_length=30, null=True)),
                ('propertyname', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fingerprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Idnumber', models.CharField(max_length=30, null=True)),
                ('FirstName', models.CharField(max_length=30, null=True)),
                ('LastName', models.CharField(max_length=30, null=True)),
                ('EntryTime', models.DateField(null=True)),
                ('ExitTime', models.DateField(null=True)),
                ('category', models.CharField(max_length=30, null=True)),
                ('propertycode', models.CharField(max_length=30, null=True)),
                ('propertyname', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EquipNumber', models.CharField(max_length=30, null=True)),
                ('EquipName', models.CharField(max_length=30, null=True)),
                ('EquipRoom', models.CharField(max_length=30, null=True)),
                ('ProductName', models.CharField(max_length=30, null=True)),
                ('EquipIdcode', models.CharField(max_length=30, null=True)),
                ('equipLocation', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rfidscan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Idnumber', models.CharField(max_length=30, null=True)),
                ('FirstName', models.CharField(max_length=30, null=True)),
                ('LastName', models.CharField(max_length=30, null=True)),
                ('EntryTime', models.DateField(null=True)),
                ('ExitTime', models.DateField(null=True)),
                ('category', models.CharField(max_length=30, null=True)),
                ('propertycode', models.CharField(max_length=30, null=True)),
                ('propertyname', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScanEquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('phoneNumber', models.CharField(max_length=30, null=True)),
                ('PresentAddress', models.CharField(max_length=30, null=True)),
                ('PermanentAddress', models.CharField(max_length=30, null=True)),
                ('equipId', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='idscan',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]