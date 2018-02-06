from rest_framework import serializers
from models import Employee, LeaveType, LeaveCredit, LeaveRequest, Status


class createSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = '__all__'



	# name = models.ForeignKey(Employee, null=True, related_name='employee_name')
	# reporter = models.ForeignKey(Employee, null=True, related_name='reporting_senior_name')
	# leave_type = models.ForeignKey(LeaveType, null=True, related_name='type')
	# from_date = models.DateField()
	# to_date = models.DateField()
	# no_days = models.IntegerField()
	# reason = models.CharField(max_length=500)
	# status = models.ForeignKey(Status,
	# 	on_delete=models.CASCADE)


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





