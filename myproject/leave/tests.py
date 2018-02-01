# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

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
