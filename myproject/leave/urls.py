from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from leave import views
# from views import ApplyForm
# urlpatterns = [
# 	    #url(r'^snippets/$', views.ApplyForm.as_view()),
# 	 url(r'^apply/user/(?P<employee_name>\w+)/$', views.ApplyForm.as_view(), name='get_user_details'),
# 	# url(r'^apply/credits/(?P<employee_name>\w+)/$', ApplyForm.as_views(), name='get_credits'),
# ]
urlpatterns = [
	url(r'^apply/user/(?P<employee_name>\w+)/$', views.UserView.as_view(), name= 'user'),
	url(r'^apply/credits/(?P<employee_name>\w+)/$', views.LeaveCreditView.as_view(), name= 'user'),
	
]
