# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-12-19 22:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20161216_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 12, 19, 22, 46, 45, 343067)),
        ),
        migrations.AlterField(
            model_name='news',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 12, 19, 22, 46, 45, 344700)),
        ),
        migrations.AlterField(
            model_name='order',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Product_Category'),
        ),
        migrations.AlterField(
            model_name='research_timeline',
            name='Activity',
            field=models.TextField(blank=True, default=datetime.datetime(2016, 12, 19, 22, 46, 45, 344236)),
        ),
        migrations.AlterField(
            model_name='research_timeline',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 12, 19, 22, 46, 45, 344203)),
        ),
    ]