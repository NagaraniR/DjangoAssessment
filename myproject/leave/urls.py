from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^apply/(?P<employee_name>\w+)/$', views.ApplyForm.as_view(), name='get_user_details'),
	url(r'^apply/(?P<employee_name>\w+)/$', views.ApplyForm.as_view(), name='get_credits'),

]