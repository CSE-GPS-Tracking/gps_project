# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-25 03:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gps_databases', '0002_auto_20200425_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(max_length=20),
        ),
    ]
