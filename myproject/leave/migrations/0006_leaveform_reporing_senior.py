# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-17 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0005_auto_20180117_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveform',
            name='reporing_senior',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
