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
	url(r'^user/(?P<employee_name>\w+)/$', views.UserView.as_view(), name= 'User'),
	url(r'^credits/(?P<employee_name>\w+)/$', views.LeaveCreditView.as_view(), name= 'credits'),
	#url(r'^apply/$', views.ApplyLeave.as_view(), name="apply"),
    url(r'^status/$', views.StatusView.as_view(), name= 'status'),
	url(r'^store/data/database/$', views.Post.as_view(), name= 'apply'),
	url(r'^validation/(?P<employee_name>\w+)/$', views.Post.as_view(), name= 'apply'),
<<<<<<< HEAD

	url(r'^approval/(?P<employee_name>\w+)/$', views.ApprovalForm.as_view(), name='approval'),
	url(r'^requests/$',views.Waiting_For_Approval.as_view(), name='requests'),
=======
	
	url(r'^approval/(?P<employee_name>\w+)/$', views.ApprovalForm.as_view(), name='approval'),
	url(r'^request/$', views.WaitngForApprovalView.as_view(), name='request'),
>>>>>>> cd0bb6cd0cc21767a418c4ef8844546a57969a7d
	# url(r'^apply/user/(?P<employee_name>\w+)/$', views.UserView.as_view(), name= 'user'),
	# url(r'^apply/credits/(?P<employee_name>\w+)/$', views.LeaveCreditView.as_view(), name= 'user'),
]
