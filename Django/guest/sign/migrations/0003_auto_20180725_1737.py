# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-07-25 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0002_auto_20180725_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(verbose_name='events time'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
