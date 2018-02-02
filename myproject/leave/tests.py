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

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json

class ReadUserTest(APITestCase):
	def setUp(self):
		self.superuser = User.objects.create_superuser('admin', 'admin@example.com', 'admin1234')
		self.client.login(username='admin', password='admin1234')
		self.user = User.objects.create(name="naga")

		def test_user(self):
			response = self.client.get('/leave/user/naga/')
			self.assertEqual(response.content, '[{"reporting_senior": "Badri","name": "naga",}]')
# class UserTest(APITestCase):
	# url = reverse('user')
	

# from __future__ import unicode_literals

# from django.test import TestCase
# from .models import LeaveRequest
# from django.core.urlresolvers import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase

# from .serializers import LeaveRequestSerializer
# # Create your tests here.

# # factory = APIRequestFactory()
# # request = factory.get('/approval/OmPrakash',{'name':'OmPrakash'},format='json')

# class ReadUserTest(APITestCase):
# 	def sutUp(self):
# 		self.superuser = LeaveRequest.objects.create_superuser('admin', 'admin@example.com', 'admin1234')
# 		self.client.login(username='admin', password='admin1234')
# 		self.user = LeaveRequest.objects.create(employee_name="OmPrakash")
# 		# self.data = {'1004', 'OmPrakash', 'omprakash@gmail.com', '2018-01-10', '1', 'Developer', 'Badri'}

# 	def test_can_read_user_list(self):
# 		response = self.client.get(reverse('approval'))
# 		self.assertEqual(response.status_code, status.HTTP_200_OK)

