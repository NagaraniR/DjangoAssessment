# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employee, LeaveType

class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        # url = reverse('account-list')
        url = "http://127.0.0.1:8000/leave/apply/2/"
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data, status.HTTP_201_CREATED)
		# response = self.client.post("http://127.0.0.1:8000/leave/apply/2/", {}, format='json')
		# self.assertEqual(response.data['name'], {})

# Create your tests here.
# factory = APIRequestFactory()
# request = factory.get('/approval/OmPrakash',{'name':'OmPrakash'},format='json')

# class LeaveRequestTest(APITestCase):
# 	def setUp(self):
# 		self.client = Client()
# 		self.username = 'admin'
# 		self.email = 'admin@gmail.com'
# 		self.password = 'test1234'
# 		self.test_user = User.objects.create_user(self.username, self.email, self.password)
# 		login = self.client.login(username=self.username, password=self.password)
# 		self.assertEqual(login, True)
	
# 	# def setUp(self):
# 	# 	user = User.objects.create(
# 	# 		code=1001
# 	# 		name ='OmPrakash',
# 	# 		reporting_senior = "Badri",)
# 	# 	type_leave = LeaveType.objects.create(
# 	# 		catagory = "Sick") 
# 	# 	status = Status.objects.create(status="Pending")
# 	# 	LeaveRequest.objects.create(
# 	# 		code=1001,
# 	# 		employee_name=user,
# 	# 		reporter = user,
# 	# 		leave_type=type_leave,
# 	# 		from_date="12-01-2018",
# 	# 		to_date="13-01-2018", 
# 	# 		no_days=1, 
# 	# 		reason="Fever", 
# 	# 		status=status)
	
# 	def test_info(self):
# 		response = client.get(reverse('approval:OmPrakash'))
# 		leave_info = LeaveRequest.objects.all()
# 		serializer = LeaveRequestSerializer(leave_info, many=True)
# 		self.assertEqual(response.data, serializer.data)
# 		self.assertEqual(response.status_code, status.HTTP_200_OK)

# from django.core.urlresolvers import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from models import Designation, User, Status, LeaveType, LeaveCredit, LeaveRequest
# from serializers import UserSerializer
# import json

# class ReadUserTest(APITestCase):
# 	client = APIClient()
# 	# def setUp(self):
# 	# 	import pdb;pdb.set_trace()
# 	# 	# self.superuser = User.objects.create_superuser('admin', 'admin@example.com', 'admin1234')
# 	# 	# self.client.login(username='admin', password='adminadmin')
# 	# 	designation1 = Designation.objects.create(code=111, name = "Python trainee")
# 	# 	designation2 = Designation.objects.create(code=112, name = "DevOps Trainee")
#  #        User.objects.create(
#  #            code = 1,
#  #             name='raja',
#  #              email='raja@example.com',
#  #               join_date="2017-07-22",
#  #                mode=True,
#  #                designation=designation1,
#  #                reporting_senior='raja')


# 	def test_user(self):
# 		import pdb;pdb.set_trace()
# 		#print "hi"
# 		response = client.get(reverse('user:naga'))
# 		# designation1 = Designation.objects.create(code=111, name = "Python trainee")
# 		# User.objects.create(
#   #           code = 1,
#   #            name='raja',
#   #             email='raja@example.com',
#   #              join_date="2017-07-22",
#   #               mode=True,
#   #               designation=designation1,
#   #               reporting_senior='raja')
# 		# designation = Designation.objects.all()
# 		# user1 = User.objects.all()
#         serializer = UserSerializer(User.objects.filter(name="naga"), many=True)
#         print "sda",serializer.data
#         #print "sdg",response.data
#         self.assertEqual(response.data, serializer.data)
# # class UserTest(APITestCase):
# 	# url = reverse('user')
	

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

