from rest_framework import serializers
from models import Employee, LeaveType, LeaveCredit, LeaveRequest, Status
# from django.db import models


class CreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = LeaveRequest
		fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Employee
		fields = "__all__"	


class LeaveTypeSerializer(serializers.ModelSerializer):

	class Meta:
		model = LeaveType
		fields = "__all__"				
		# fields = ("from_date", "to_date", "no_days", "reason")

	# def create(self, validated_data):
	# 	import pdp;pdp.set_trace()
	# 	name = validated_data.data.get("name")
	# 	validated_data.pop("name")
	# 	reporter = validated_data.data.get("reporter")
	# 	validated_data.pop("reporter")
	# 	leave_type = validated_data.data.get("leave_type")
	# 	validated_data.pop("leave_type")
	# 	status = validated_data.data.get("status")
	# 	validated_data.pop("status")
	# 	return models.LeaveRequest.objects.create(name=name,
	# 	reporter=reporter,
	# 	leave_type=leave_type,
	# 	from_date=from_date,
	# 	to_date=to_date,
	# 	no_days=no_days,
	# 	reason=reason,
	# 	status=status,
	# 	 **validated_data)		




# 		{
#         "id": 1,
#         "name": "nagarani",
#         "reporter": "a@b123.com",
# "leave_type","Personal",
# "from_date" :12-03-2018
# 	"to_date":13-03-2018
# 	"no_days":2
# 	"reason" :"fever"
#     }
# class ApplySerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Employee
# 		fields = ('name','email')

# class UserSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Employee
# 		fields = ('name', 'reporting_senior')

# # class LeaveCreditSerializer(serializers.ModelSerializer):
# # 	leave_type_name = serializers.CharField(source='leave_type.catagory')
# # 	class Meta:
# # 		model = LeaveCredit
# # 		fields = "__all__"

# # class StatusSerializer(serializers.ModelSerializer):
# # 	class Meta:
# # 		model = Status
# # 		fields = "__all__"
# class LeaveRequestSerializer2(serializers.ModelSerializer):
# 	employee_name = serializers.CharField(source='employee_name.name')
# 	reporter = serializers.CharField(source='reporter.name')
# 	leave_type_name = serializers.CharField(source='leave_type.catagory')
# 	approval_status = serializers.CharField(source='status.status')




# class LeaveRequestSerializer2(serializers.ModelSerializer):
# 	employee_name = serializers.CharField(source='employee_name.name')
# 	reporter = serializers.CharField(source='reporter.name')
# 	leave_type_name = serializers.CharField(source='leave_type.catagory')
# 	approval_status = serializers.CharField(source='status.status')

# 	class Meta:
# 		model = Status
# 		fields = '__all__'


# ##for Approval serializer creation 
# class LeaveRequestSerializer(serializers.ModelSerializer):
# 	employee_name = serializers.CharField(source='employee_name.name')
# 	reporter = serializers.CharField(source='reporter.name')
# 	leave_type_name = serializers.CharField(source='leave_type.catagory')
# 	approval_status = serializers.CharField(source='status.status')
# 	class Meta:
# 		model=LeaveRequest
# 		fields ="__all__"
	

##for Approval serializer creation 
# class LeaveRequestSerializer(serializers.ModelSerializer):
# 	employee_name = serializers.CharField(source='employee_name.name')
# 	reporter = serializers.CharField(source='reporter.name')
# 	leave_type_name = serializers.CharField(source='leave_type.catagory')
# 	approval_status = serializers.CharField(source='status.status')
	
# 	class Meta:
# 		model=LeaveRequest
# 		fields ="__all__"
		
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





