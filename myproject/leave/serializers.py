from rest_framework import serializers
<<<<<<< HEAD
from models import LeaveRequest, User
=======
from models import User, LeaveCredit
>>>>>>> 28df6504d02b6d1322b269961832646c425cd5fe


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('name', 'reporting_senior')

class LeaveCreditSerializer(serializers.ModelSerializer):
	leave_type_name = serializers.CharField(source='leave_type.catagory')
	class Meta:
		model = LeaveCredit
		fields = ('leave_type_name', 'available')