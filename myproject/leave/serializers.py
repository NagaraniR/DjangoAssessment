from rest_framework import serializers
from models import User, LeaveCredit, LeaveRequest, Status

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('name', 'reporting_senior')

class LeaveCreditSerializer(serializers.ModelSerializer):
	leave_type_name = serializers.CharField(source='leave_type.catagory')
	class Meta:
		model = LeaveCredit
		fields = "__all__"

class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = "__all__"

class LeaveRequestSerializer2(serializers.ModelSerializer):
	employee_name = serializers.CharField(source='employee_name.name')
	reporter = serializers.CharField(source='reporter.name')
	leave_type_name = serializers.CharField(source='leave_type.catagory')
	approval_status = serializers.CharField(source='status.status')

	class Meta:
		model = Status
		fields = '__all__'

##for Approval serializer creation 
class LeaveRequestSerializer(serializers.ModelSerializer):
	employee_name = serializers.CharField(source='employee_name.name')
	reporter = serializers.CharField(source='reporter.name')
	leave_type_name = serializers.CharField(source='leave_type.catagory')
	approval_status = serializers.CharField(source='status.status')
	
	class Meta:
		model=LeaveRequest
		fields ="__all__"
		
# fields = ('employee_name', 'reporter', 'leave_type_name', 'from_date', 
# 	'to_date', 'no_days', 'reason', 'approval_status')

# class UserDetailsSerializers(serializers.Serializer):
# 	user_details = UserSerializer(many=True)
# 	leave_credits = LeaveCreditSerializer(many=True)				

# class TweetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tweet

# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article

# class TimelineSerializer(serializers.Serializer):
#     tweets = TweetSerializer(many=True)
#     articles = ArticleSerializer(many=True)


