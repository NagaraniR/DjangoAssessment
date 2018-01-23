from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^apply/(?P<name>\w+)/$', views.apply, name='apply'),
	#url(r'^leave_response/(?P<employee_name>\w+)/s', views.leave_response, name='response' )
]