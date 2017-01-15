# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 10:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20170114_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('sales_staff', 'sales staff'), ('sales_man', 'sales manager'), ('admin', 'administrator'), ('design', 'desin_staff'), ('tech', 'tech_manager')),
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 1, 15, 10, 5, 15, 395456)),
        ),
        migrations.AlterField(
            model_name='news',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 1, 15, 10, 5, 15, 397237)),
        ),
        migrations.AlterField(
            model_name='research_timeline',
            name='Activity',
            field=models.TextField(blank=True, default=datetime.datetime(2017, 1, 15, 10, 5, 15, 396713)),
        ),
        migrations.AlterField(
            model_name='research_timeline',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 1, 15, 10, 5, 15, 396681)),
        ),
    ]