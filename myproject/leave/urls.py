from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from leave import views


urlpatterns = [


url(r'^employee/$', views.Employee.as_view(), name= 'employee'),
url(r'^types/$', views.Leave.as_view(), name= 'leave_types'),
url(r'^apply/$', views.Apply.as_view(), name = 'apply'),
url(r'^details/$', views.Detail.as_view(), name = 'details'),
url(r'^deny/$', views.DenyView.as_view(), name='leave_deny'),
url(r'^approve/$', views.ApproveView.as_view(), name='leave_approve'),
url(r'^available/(?P<pk>\d+)/$', views.LeaveBalance.as_view(),name='available_leaves'),
url(r'^request/(?P<pk>\d+)/$', views.LeaveRequestView.as_view(), name='leave_request'),
]
