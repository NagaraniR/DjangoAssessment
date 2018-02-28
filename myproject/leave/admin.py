# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Designation, Employee, Status, LeaveType, LeaveCredit, LeaveRequest

# Register your models here.
admin.site.register(Designation)
admin.site.register(Employee)
admin.site.register(Status)
admin.site.register(LeaveType)
admin.site.register(LeaveCredit)
admin.site.register(LeaveRequest)
