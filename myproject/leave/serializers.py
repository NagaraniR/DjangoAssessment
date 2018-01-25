from rest_framework import serializers
from models import User, LeaveCredit, LeaveRequest


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = "__all__"

class LeaveCreditSerializer(serializers.ModelSerializer):
	leave_type_name = serializers.CharField(source='leave_type.catagory')
	class Meta:
		model = LeaveCredit
		fields = ('leave_type_name', 'available')





##for Approval serializer creation 
class LeaveRequestSerializer(serializers.ModelSerializer):
	employee_name = serializers.CharField(source='employee_name.name')
	reporter = serializers.CharField(source='reporter.name')
	leave_type_name = serializers.CharField(source='leave_type.catagory')
	approval_status = serializers.CharField(source='status.status')
	class Meta:
		model=LeaveRequest
		fields = ('employee_name', 'reporter', 'leave_type_name', 'from_date', 
			'to_date', 'no_days', 'reason', 'approval_status')
