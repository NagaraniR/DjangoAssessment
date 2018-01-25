from rest_framework import serializers
from models import User, LeaveCredit


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('name', 'reporting_senior')

class LeaveCreditSerializer(serializers.ModelSerializer):
	leave_type_name = serializers.CharField(source='leave_type.catagory')
	class Meta:
		model = LeaveCredit
		fields = ('leave_type_name', 'available')

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

