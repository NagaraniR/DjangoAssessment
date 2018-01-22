# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-22 05:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0009_auto_20180118_0427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveCredit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('no_days', models.IntegerField()),
                ('reason', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('catagory', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('join_date', models.DateField()),
                ('mode', models.BooleanField()),
                ('reporting_senior', models.CharField(max_length=30)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave.Designation')),
            ],
        ),
        migrations.RemoveField(
            model_name='leaveform',
            name='reporing_senior',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='LeaveForm',
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='employee_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_name', to='leave.User'),
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='leave_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leave_type', to='leave.LeaveType'),
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='reporter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reporter', to='leave.User'),
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave.Status'),
        ),
        migrations.AddField(
            model_name='leavecredit',
            name='leave_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave.LeaveType'),
        ),
        migrations.AddField(
            model_name='leavecredit',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave.User'),
        ),
    ]