from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from leave import views


urlpatterns = [

url(r'^employee/$', views.User.as_view(), name= 'employee'),
url(r'^login/$', views.LoginCheck.as_view(), name= 'login'),
url(r'^types/$', views.Leave.as_view(), name= 'leave_types'),
url(r'^apply/$', views.Apply.as_view(), name = 'apply'),
url(r'^details/$', views.Detail.as_view(), name = 'details'),
url(r'^approval/awaiting/$', views.Approval.as_view(), name = 'details'),
url(r'^pending/requests/$', views.LeaveRequestView.as_view(), name='view_request'),
url(r'^deny/$', views.DenyView.as_view(), name='leave_deny'),
url(r'^approve/$', views.ApproveView.as_view(), name='leave_approve'),
url(r'^availables/$', views.LeaveBalance.as_view(),name='available_leaves'),
]
urlpatterns = format_suffix_patterns(urlpatterns)