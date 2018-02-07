# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-07 09:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0005_leaverequest_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaverequest',
            name='code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emp_code', to='leave.Employee'),
        ),
        migrations.AlterField(
            model_name='designation',
            name='code',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='code',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='leavetype',
            name='code',
            field=models.IntegerField(unique=True),
        ),
    ]