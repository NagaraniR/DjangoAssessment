from rest_framework import serializers
from models import LeaveRequest, User


class UserLeave(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'
