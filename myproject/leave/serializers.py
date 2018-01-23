from rest_framework import serializers
from models import LeaveRequest


class UserLeave(serializers.ModelSerializer):
	class Meta:
		model = LeaveRequest
		fields = 'employee_name', 
