# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 20:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20170114_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 1, 14, 20, 25, 39, 992152)),
        ),
        migrations.AlterField(
            model_name='news',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 1, 14, 20, 25, 39, 993974)),
        ),
        migrations.AlterField(
            model_name='research_timeline',
            name='Activity',
            field=models.TextField(blank=True, default=datetime.datetime(2017, 1, 14, 20, 25, 39, 993438)),
        ),
        migrations.AlterField(
            model_name='research_timeline',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 1, 14, 20, 25, 39, 993374)),
        ),
    ]