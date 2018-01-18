# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-18 04:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0008_leaveform_reporing_senior'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveform',
            name='employee',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='leaveform',
            name='reporing_senior',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave.Employee'),
        ),
    ]