from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from leave import views

urlpatterns = [
	url(r'^approve/(?P<pk>\d+)/$', views.Approve.as_view(), name='approve'),
	url(r'^apply/(?P<pk>\d+)/$', views.ApplyView.as_view(), name= 'user'),
]
