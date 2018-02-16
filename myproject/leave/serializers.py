from rest_framework import serializers
from models import Employee, LeaveType, LeaveCredit, LeaveRequest, Status, LeaveCredit
# from django.db import models

class LeaveTypeSerializer(serializers.ModelSerializer):

	class Meta:
		model = LeaveType
		fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Employee
		fields = ['id', 'name', 'reporting_senior', 'email']

class LeaveCreditSerializer(serializers.ModelSerializer):
	
	leave_type = LeaveTypeSerializer()
	name = EmployeeSerializer()

	class Meta:
		model = LeaveCredit
		fields = ['id', 'name', 'leave_type', 'available']

<<<<<<< HEAD
class LeaveRequestSerializer(serializers.ModelSerializer):
=======
class EmployeeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Employee
		fields = ('name', 'reporting_senior')	
>>>>>>> 3aba837e4312634cb5d03dd7eac18100a160d4a5

	leave_type = LeaveTypeSerializer()
	name = EmployeeSerializer()

	class Meta:
		model = LeaveRequest
		fields = "__all__"				

class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = "__all__"
	

			


	