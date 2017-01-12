# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-02 18:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20161219_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Product',
        ),
        migrations.AlterField(
            model_name='blog',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 1, 2, 18, 29, 8, 441220)),
        ),
        migrations.AlterField(
            model_name='news',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 1, 2, 18, 29, 8, 442919)),
        ),
        migrations.AlterField(
            model_name='research_timeline',
            name='Activity',
            field=models.TextField(blank=True, default=datetime.datetime(2017, 1, 2, 18, 29, 8, 442453)),
        ),
        migrations.AlterField(
            model_name='research_timeline',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 1, 2, 18, 29, 8, 442424)),
        ),
    ]