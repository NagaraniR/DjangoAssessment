# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from models import Status,Employee,LeaveType
from django.core.serializers.python import Serializer
#from serializers import UserSerializer
from rest_framework.response import Response
from .serializers import CreateSerializer, EmployeeSerializer, LeaveTypeSerializer
import datetime
# from rest_framework.generics import CreateAPIView
# import requests


class ApplyView(APIView):

  def get(self, request, pk, format=None):

    employee = Employee.objects.filter(id=pk)
    leave_types = LeaveType.objects.all()
    serializer = EmployeeSerializer(employee, many=True)
    leave_type_serializer = LeaveTypeSerializer(leave_types, many=True)

    return Response({"employee":serializer.data,"leave_types":leave_type_serializer.data})

    
  def post(self, request, pk, format=None):
    user = Employee.objects.get(id=pk)
    # request.data["name"] = user.id
    # name = request.data["name"]
    # user = Employee.objects.get(name = request.data["name"])
    request.data["name"] = user.id
    request.data["reporter"] = user.reporting_senior.id
    leave = LeaveType.objects.get(catagory = request.data["leave_type"])
    request.data["leave_type"] = leave.id
    from_date = datetime.datetime.strptime(self.request.data.get('from_date'), "%Y-%m-%d")
    to_date = datetime.datetime.strptime(self.request.data.get('to_date'), "%Y-%m-%d")
    no_days = abs((to_date-from_date).days)
    request.data["no_days"] = no_days
    status = Status.objects.get(code=1)
    request.data["status"]= status.id
    serializer = CreateSerializer(data=request.data, many=False)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
    return JsonResponse(serializer.errors)


# class ApplyView(APIView)



# class Post(APIView):

#     def post(self, request):    
#         # response = requests.get(request.data)
#         # json_data = json.loads(response.text)
#         #value = request.data.encode("utf-8")
#         name = request.data["name"]

#         reporting_senior = request.data["reporting_senior"]
#         credits = request.data["credits"]
#         fromDate = request.data["fromDate"]
#         toDate = request.data["toDate"]
#         reason = request.data["reason"]
#         days = request.data["days"]
#         status = request.data["status"]
#         leave_request = LeaveRequest.objects.create(
#             employee_name= User.objects.get(name=name),
#             reporter = User.objects.get(name=reporting_senior), 
#             leave_type = LeaveType.objects.get(id=credits),
#             from_date = fromDate,
#             to_date = toDate,
#             no_days = days ,
#             reason = reason,
#             status = Status.objects.get(id=status)
#             )
# <<<<<<< HEAD
#         leave_request.save()
#         return Response("returned")

# =======
# >>>>>>> bc86fafb300efa29b19f7206ca117bc6ae4ff3be

#         leave_request.save()
#         return Response("returned")
#         values = json.loads(request.body)
#         # name = data.get("name")
#         print "sdff";
#         user = User.objects.all()
#         return Response(User)

# ##For Approval  
# class ApprovalForm(APIView):

#     def get(self, request, employee_name):
#         user = LeaveRequest.objects.filter(employee_name__name=employee_name)
#         user = LeaveRequestSerializer(user, many=True)
#         return Response(user.data)

#     def put(self, request, employee_name):
#         user = LeaveRequest.objects.filter(employee_name__name=employee_name)
#         status = Status.objects.get(status=request.data["status"])
#         serializer = LeaveRequestSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class WaitngForApprovalView(APIView):
#     def get(self,request):
#         user = LeaveRequest.objects.all()
#         pending_user = LeaveRequestSerializer(user, many=True)
#         return Response(pending_user.data) 

# class UserView(APIView):
#     def get(self, request, employee_name):
#         #import pdb;pdb.set_trace()
#         user = User.objects.filter(name=employee_name)
#         user_serializer = UserSerializer(user, many=True)
#         return Response(user_serializer.data)

# class LeaveCreditView(APIView):
#     def get(self, request, employee_name):
#         credits = LeaveCredit.objects.filter(user_name__name=employee_name)
#         credit_serializer = LeaveCreditSerializer(credits, many=True )
#         return Response(credit_serializer.data)

# class StatusView(APIView):
#     def get(self, request):
#         status = Status.objects.all()
#         status_serializer = StatusSerializer(status, many=True)
#         return Response(status_serializer.data)

# class LeaveRequestView(APIView):

#     def get(self,request):        
#         leave_request = LeaveRequest.objects.all()
#         leave_request_serializer = LeaveRequestSerializer2(status, many=True)
#         return Response(leave_request_serializer.data)

# @api_view(['GET', 'POST'])
# def apply_leave(self, request):
#     return

    	#import pdb;pdb.set_trace()
    	# user = User.objects.filter(name=employee_name)
    	# 
      #  credits = LeaveCredit.objects.filter(user_name__name=employee_name)
     #    user_serializer = UserSerializer(user, many=True)
     #    credit_serializer = LeaveCreditSerializer(credits, many=True )
     #    user_data = JSONRenderer().render(user_serializer.data)
     #    name_info=json.loads(user_data)
     #    credits_data = JSONRenderer().render(credit_serializer.data)
     #    leave_credit=json.loads(credits_data)
     #    return Response({'user_data': name_info, 'credits_data':leave_credit}, template_name='leave/apply.html')

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
