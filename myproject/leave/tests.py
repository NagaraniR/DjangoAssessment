# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import User, LeaveRequest
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from .serializers import LeaveRequestSerializer
# Create your tests here.

# factory = APIRequestFactory()
# request = factory.get('/approval/OmPrakash',{'name':'OmPrakash'},format='json')

class LeaveRequestTest(APITestCase):
	def setUp(self):
		self.client = Client()
		self.username = 'admin'
		self.email = 'admin@gmail.com'
		self.password = 'test1234'
		self.test_user = User.objects.create_user(self.username, self.email, self.password)
		login = self.client.login(username=self.username, password=self.password)
		self.assertEqual(login, True)
	
	# def setUp(self):
	# 	user = User.objects.create(
	# 		code=1001
	# 		name ='OmPrakash',
	# 		reporting_senior = "Badri",)
	# 	type_leave = LeaveType.objects.create(
	# 		catagory = "Sick") 
	# 	status = Status.objects.create(status="Pending")
	# 	LeaveRequest.objects.create(
	# 		code=1001,
	# 		employee_name=user,
	# 		reporter = user,
	# 		leave_type=type_leave,
	# 		from_date="12-01-2018",
	# 		to_date="13-01-2018", 
	# 		no_days=1, 
	# 		reason="Fever", 
	# 		status=status)
	
	def test_info(self):
		response = client.get(reverse('approval:OmPrakash'))
		leave_info = LeaveRequest.objects.all()
		serializer = LeaveRequestSerializer(leave_info, many=True)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)