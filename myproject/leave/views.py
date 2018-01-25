# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from models import Designation, User, Status, LeaveType, LeaveCredit, LeaveRequest
from serializers import UserSerializer, LeaveCreditSerializer, LeaveRequestSerializer
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import json

class ApplyForm(APIView):
    
	def get(self, request, employee_name):
		queryset_one = User.objects.filter(name=employee_name)
		user_serializer = UserSerializer(queryset_one, many=True)
		return Response(user_serializer.data)





##For Approval  
class ApprovalForm(APIView):

    def get(self, request, employee_name):
       
        user = LeaveRequest.objects.filter(employee_name__name=employee_name)
        user = LeaveRequestSerializer(user, many=True)
        return Response(user.data)

    # def put(self, request, employee_name):
    #     user = LeaveRequest.objects.filter(employee_name__name=employee_name)
    #     serializer = LeaveRequestSerializer(user, data=request.DATA)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# def getCredits(self, request, employee_name):	
	#     queryset_two = LeaveCredit.objects.filter(user_name__name = employee_name)
	#     leave_credit_serializer = LeaveCreditSerializer(queryset_two, many=True)
	#     return JsonResponse(leave_credit_serializer.data, safe=False)
    # @api_view(['GET', 'POST', 'PUT', 'DELETE'])	
    # #@renderer_classes((JSONRenderer,))
    # def person_list(request, employee_name):
    #     if request.method == 'GET':
    #         #email = request.GET.get('email')
    #         if employee_name:
    #             user = User.objects.filter(name=employee_name)
    #         # else:
    #         #     user = User.objects.all()
    #         serializer = UserSerializer(user, many=True)
    #         data = serializer.data
    #         return Response({'user_data':data},apply.html)
