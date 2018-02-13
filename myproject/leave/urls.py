from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from leave import views


urlpatterns = [


url(r'^user/leave/apply/employee/(?P<pk>\d+)/$', views.ApplyGetView.as_view(), name= 'user'),
url(r'^apply/$', views.ApplyPostView.as_view(), name = 'apply'),
url(r'^user/leave/history/(?P<pk>\d+)/$', views.UserHistoryView.as_view(), name = 'apply'),
url(r'^WAPPR/(?P<pk>\d+)/$', views.WAPPRView.as_view(), name = 'apply'),
	
	url(r'^deny/$', views.DenyRequest.as_view(), name='leave_deny'),
	url(r'^approve/$', views.ApproveRequest.as_view(), name='leave_approve'),
	url(r'^available/(?P<pk>\d+)/$', views.LeaveBalance.as_view(),name='available_leaves'),
	url(r'^request/(?P<pk>\d+)/$', views.LeaveRequestView.as_view(), name='leave_request'),
]
