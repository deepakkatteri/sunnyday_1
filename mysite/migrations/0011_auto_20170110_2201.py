# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 22:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_auto_20170110_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 1, 10, 22, 1, 48, 531704)),
        ),
        migrations.AlterField(
            model_name='news',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 1, 10, 22, 1, 48, 533712)),
        ),
        migrations.AlterField(
            model_name='research_timeline',
            name='Activity',
            field=models.TextField(blank=True, default=datetime.datetime(2017, 1, 10, 22, 1, 48, 533173)),
        ),
        migrations.AlterField(
            model_name='research_timeline',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 1, 10, 22, 1, 48, 533142)),
        ),
    ]