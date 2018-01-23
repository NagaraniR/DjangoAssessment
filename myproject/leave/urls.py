from django.conf.urls import url
from . import views


urlpatterns = ['app.views',
	url(r'^apply/(?P<employee_name>\w+)/user/$', ApplyForm.getUser.asview(), name='get_user_details'),
	url(r'^apply/(?P<employee_name>\w+)/credits/$', ApplyForm.getCredits.asview(), name='get_credits'),
]