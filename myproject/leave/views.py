# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from models import Designation, User, Status, LeaveType, LeaveCredit, LeaveRequest
from serializers import UserSerializer, LeaveCreditSerializer
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

class ApplyForm(APIView):

	@api_view(['GET'])
	def getUser(request, employee_name):
		queryset_one = User.objects.filter(name = employee_name)
		user_serializer = UserSerializer(queryset_one, many=True)
		return JsonResponse(user_serializer.data, safe = False)

	def getCredits(request, employee_name):	
	    queryset_two = LeaveCredit.objects.filter(user_name__name = employee_name)
	    leave_credit_serializer = LeaveCreditSerializer(queryset_two, many=True)
	    return JsonResponse(leave_credit_serializer.data, safe=False)
	

	
