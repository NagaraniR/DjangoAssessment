# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from models import Designation, User, Status, LeaveType, LeaveCredit, LeaveRequest
from serializers import UserSerializer, LeaveCreditSerializer
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

class ApplyForm(generics.ListCreateAPIView):

    queryset = User.objects.all()
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, employee_name):
    	user = User.objects.filter(name=employee_name)
    	credits = LeaveCredit.objects.filter(user_name__name=employee_name)
        user_serializer = UserSerializer(user, many=True)
        credit_serializer = LeaveCreditSerializer(credits, many=True )
        user_data = user_serializer.data
        credits_data = credit_serializer.data
        return Response({'user_data': user_data, 'credits_data':credits_data}, template_name='leave/apply.html')

    def post(self, request):
    	


# class ApplyForm(generics.ListCreateAPIView):

# 	#def get(self, request)
# 	#@api_view(['GET'])
# 	def list(self, request, employee_name):
# 		queryset_one = User.objects.filter(name = employee_name)
# 		user_serializer = UserSerializer(queryset_one, many=True)
# 		return Response(user_serializer.data)

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
