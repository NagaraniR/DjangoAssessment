from rest_framework import serializers
from models import Employee, LeaveType, LeaveCredit, LeaveRequest, Status, LeaveCredit
# from django.db import models


class LeaveRequestSerializer(serializers.ModelSerializer):

	class Meta:
		model = LeaveRequest
		fields = "__all__"

class LeaveCreditSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = LeaveCredit
		fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Employee
		fields = ('name', 'reporting_senior')	

class LeaveTypeSerializer(serializers.ModelSerializer):

	class Meta:
		model = LeaveType
		fields = "__all__"				

class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = "__all__"
	

			


	