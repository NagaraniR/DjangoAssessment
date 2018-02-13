# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework import status
from models import Status, Employee, LeaveType, LeaveRequest, LeaveCredit
from django.core.serializers.python import Serializer
from rest_framework.response import Response
from .serializers import LeaveRequestSerializer, EmployeeSerializer, LeaveTypeSerializer, LeaveCreditSerializer
import datetime
from rest_framework.response import Response
from rest_framework.views import exception_handler


class ApplyGetView(APIView):
    
    def get(self, request, pk, format=None):
        try:
            # import pdb;pdb.set_trace()
            response = exception_handler(request, pk)
            if response is not None:
                employee = Employee.objects.filter(id=pk)
                leave_types = LeaveType.objects.all()
                serializer = EmployeeSerializer(employee, many=True)
                leave_type_serializer = LeaveTypeSerializer(leave_types, many=True)
                return Response({"employee":serializer.data,"leave_types":leave_type_serializer.data})
            return Response(response)
        except Exception as exception:
            template = "An exception of type readRailInfo function {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            return Response(message)

class ApplyPostView(APIView):    
    
    def post(self, request, format=None):
        try:
            # response = exception_handler(request)
            # print "sad",response
            # import pdb;pdb.set_trace()
            print "kjzhf", request.data
            user = Employee.objects.get(name=request.data["name"])
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
            serializer = LeaveRequestSerializer(data=request.data, many=False)
            if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data)
            return JsonResponse(serializer.errors)
        except Exception as exception:
                    template = "An exception of type readRailInfo function {0} occurred. Arguments:\n{1!r}"
                    message = template.format(type(exception).__name__, exception.args)
                    return Response(message)

class UserHistoryView(APIView):

    def get(self,request, pk, format=None):
        try:
            # import pdb;pdb.set_trace()
            employee = Employee.objects.get(id=pk)
            employee_history = LeaveRequest.objects.filter(name=employee.id)
            leave_history_serializer = LeaveRequestSerializer(employee_history, many=True)
            return Response(leave_history_serializer.data)
        except Exception as exception:
                    template = "An exception of type readRailInfo function {0} occurred. Arguments:\n{1!r}"
                    message = template.format(type(exception).__name__, exception.args)
                    return Response(message)

class WAPPRView(APIView):

    def get(self, request, pk, format=None):
        try:
            # import pdb;pdb.set_trace()
            reporter = Employee.objects.get(id=pk)
            employees = Employee.objects.filter(reporting_senior=reporter).values_list("id", flat=True)
            # requests = LeaveRequest.objects.filter(name=employees)
            waiting_for_approval = LeaveRequest.objects.filter(name__in=employees)
            status = Status.objects.get(code=101)
            pending_serializer = LeaveRequestSerializer(waiting_for_approval, many=True)
            return Response(pending_serializer.data)
        except Exception as exception:
            template = "An exception of type readRailInfo function {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            return Response(message)
          
class LeaveBalance(APIView):

    def get(self, request, pk, format=None):
        try:
            balance = LeaveCredit.objects.filter(name=pk)
            serializer = LeaveCreditSerializer(balance, many=True)
            return Response({"Leave available":serializer.data})
        except Exception as exception:
            template = "An exception of type function {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            return Response(message)

class LeaveRequestView(APIView):

    def get(self, request, pk, format=None):
        try:
            # import pdb;pdb.set_trace()
            leave_id = LeaveRequest.objects.get(id=pk)
            leave_serializer = LeaveRequestSerializer(leave_id, many=False)
            return Response(leave_serializer.data)
        except Exception as exception:
            template = "An exception of type function {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            return Response(message)

class DenyRequest(APIView):
    
    def put(self,request, format=None):
        try:
            user = LeaveRequest.objects.get(id=request.data["id"])
            if user:
                status = Status.objects.get(code=101)
                if user.status == status:
                    serializer = LeaveRequestSerializer(user)
                    return Response(serializer.data)
                else:
                    user.status = status
                    user.save()
                    serializer = LeaveRequestSerializer(user)
                    return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except Exception as exception:
            template = "An exception of type function {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            return Response(message)

class ApproveRequest(APIView):

    # def LOP(self, user):
    def check_leave_balance(self, user):
        # import pdb;pdb.set_trace()
        user_leave_balance = LeaveCredit.objects.get(name=user.name, leave_type=user.leave_type)
        if user_leave_balance.available >= 0:
            available = int(user_leave_balance.available) 
            no_days = int(user.no_days)
            available -= no_days
            user_leave_balance.available = long(available)
            user_leave_balance.save()
        return user

    def put(self,request, format=None):
        try:
            user = LeaveRequest.objects.get(id=request.data["id"])
            if user:
                status = Status.objects.get(code=100)
                if user.status == status:
                    serializer = LeaveRequestSerializer(user)
                else:
                    user_data = self.check_leave_balance(user)
                    user_data.status = status
                    user_data.save()
                    serializer = LeaveRequestSerializer(user_data)
                    return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except Exception as exception:
            template = "An exception of type function {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            return Response(message)
