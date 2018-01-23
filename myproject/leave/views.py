# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from rest_framework.views import View
from models import Designation, User, Status, LeaveType, LeaveCredit, LeaveRequest
from serializers import UserLeave
from django.http import HttpResponse, JsonResponse
from django.views import generic

def apply(request, employee_name):
	queryset = User.objects.filter(name = employee_name)
	serializer = UserLeave(queryset, many=True)
	return JsonResponse(serializer.data, safe=False)
	

	
