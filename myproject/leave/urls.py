from django.conf.urls import url
from . import views


<<<<<<< HEAD
urlpatterns = [
	url(r'^apply/(?P<name>\w+)/$', views.apply, name='apply'),
	#url(r'^leave_response/(?P<employee_name>\w+)/s', views.leave_response, name='response' )
=======
urlpatterns = ['app.views',
	url(r'^apply/(?P<employee_name>\w+)/user/$', ApplyForm.getUser.asview(), name='get_user_details'),
	url(r'^apply/(?P<employee_name>\w+)/credits/$', ApplyForm.getCredits.asview(), name='get_credits'),
>>>>>>> 28df6504d02b6d1322b269961832646c425cd5fe
]