# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework import status
from models import Status,Employee,LeaveType,LeaveRequest
from django.core.serializers.python import Serializer
from rest_framework.response import Response
from .serializers import CreateSerializer, EmployeeSerializer, LeaveTypeSerializer
import datetime


class ApplyView(APIView):

  def get(self, request, pk, format=None):
    employee = Employee.objects.filter(id=pk)
    leave_types = LeaveType.objects.all()
    serializer = EmployeeSerializer(employee, many=True)
    leave_type_serializer = LeaveTypeSerializer(leave_types, many=True)

    return Response({"employee":serializer.data,"leave_types":leave_type_serializer.data})
    
  def post(self, request, pk, format=None):
    user = Employee.objects.get(id=pk)
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

class Approve(APIView):

    def get_leaves(self, pk):
        try:
            return LeaveRequest.objects.get(id=pk)
        except LeaveRequest.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_leaves(pk)
        user = createSerializer(user)
        return Response(user.data)

    def put(self,request, pk, format=None):
        user = self.get_leaves(pk)
        status = Status.objects.get(status=request.data["status"])
        request.data["status"] = status.status
        serializer = createSerializer(request.data, many=False) 
        if serializer.is_valid(raise_exception=True):
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors)

        # user = LeaveRequest.objects.get(id=request.data["id"])
        # status = Status.objects.get(status=request.data["status"])
        # user.status = status
        # user.save()
        # serializer = createSerializer(user)
        # return Response(serializer.data)
