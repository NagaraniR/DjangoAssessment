from rest_framework import serializers
from models import Employee, LeaveType, LeaveCredit, LeaveRequest, Status
# from django.db import models


class LeaveRequestSerializer(serializers.ModelSerializer):

	class Meta:
		model = LeaveRequest
		fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Employee
		fields = "__all__"	


class LeaveTypeSerializer(serializers.ModelSerializer):

	class Meta:
		model = LeaveType
		fields = "__all__"				


			


	