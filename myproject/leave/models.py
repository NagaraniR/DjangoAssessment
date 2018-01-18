# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
#class LeaveTypeForm()
#REPORTING_SENIOR_CHOICES = [
#('Badri','Badri'),
#('Jai Srinivasan','Jai Srinivasan')
#]

#class LeaveForm(models.Model):
#	name = models.CharField(max_length=30)
#	reporing_senior = models.CharField(max_length=30, choices=REPORTING_SENIOR_CHOICES)

class Employee(models.Model):
	name = models.CharField(max_length = 30)
	email = models.CharField(max_length = 30)
	
	def __str__(self):
		return self.name

class LeaveForm(models.Model):
	reporing_senior = models.ForeignKey(Employee,
		on_delete=models.CASCADE)
	employee = models.CharField(max_length=30)
	date_from = models.DateField()
	date_to = models.DateField()
	no_days_or_hours = models.IntegerField()
	current_balance = models.FloatField(max_length=10)
	applied = models.IntegerField()
	balance_after_approval = models.IntegerField()
	lop = models.IntegerField()
