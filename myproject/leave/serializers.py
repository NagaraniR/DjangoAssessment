from rest_framework import serializers
from models import Employee, LeaveType, LeaveCredit, LeaveRequest, Status, LeaveCredit
# from django.db import models

class LeaveTypeSerializer(serializers.ModelSerializer):

	class Meta:
		model = LeaveType
		fields = "__all__"

class _EmployeeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Employee
		fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):

	reporting_senior = _EmployeeSerializer(read_only=True)

	class Meta:
		model = Employee
		fields = ('name', 'reporting_senior')	


class LeaveCreditSerializer(serializers.ModelSerializer):
	
	leave_type = LeaveTypeSerializer()
	name = EmployeeSerializer()

	class Meta:
		model = LeaveCredit
		fields = ['id', 'name', 'leave_type', 'available']

class StatusSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Status
		fields = "__all__"

class LeaveRequestSerializer(serializers.ModelSerializer):

	leave_type = LeaveTypeSerializer()
	name = EmployeeSerializer()
	status = StatusSerializer()

	class Meta:
		model = LeaveRequest
		fields = "__all__"				


	

			


	