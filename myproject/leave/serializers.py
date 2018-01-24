from rest_framework import serializers
from models import User, LeaveCredit


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = "__all__"

class LeaveCreditSerializer(serializers.ModelSerializer):
	leave_type_name = serializers.CharField(source='leave_type.catagory')
	class Meta:
		model = LeaveCredit
		fields = ('leave_type_name', 'available')