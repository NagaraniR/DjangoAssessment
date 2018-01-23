# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from rest_framework.views import View
from models import Designation, User, Status, LeaveType, LeaveCredit, LeaveRequest
from serializers import UserSerializer, LeaveSerializer
from django.http import HttpResponse, JsonResponse
from django.views import generic

def apply(request, employee_name):
	queryset_one = User.objects.filter(name = employee_name)
	user_serializer = UserSerializer(queryset_one, many=True)
	queryset_two = LeaveType.objects.all()
	leave_serializer = LeaveSerializer(queryset_two, many=True)
	return JsonResponse(leave_serializer.data, safe=False)
	

	
