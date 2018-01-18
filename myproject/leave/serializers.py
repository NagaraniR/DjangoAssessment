from rest_framework import serializers
from models import LeaveForm


class UserLeave(serializers.ModelSerializer):
	class Meta:
		model = LeaveForm
		fields = '__all__'
