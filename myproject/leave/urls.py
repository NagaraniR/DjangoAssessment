from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^apply/(?P<employee_name>\w+)/$', views.apply, name='apply'),
]