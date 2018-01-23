from rest_framework import serializers
from models import User, LeaveType


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('name', 'reporting_senior')

class LeaveSerializer(serializers.ModelSerializer):
	class Meta:
		model = LeaveType
		fields = ('catagory',)