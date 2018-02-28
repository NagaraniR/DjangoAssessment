# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.test import APITestCase, APIClient
from . import views
from models import LeaveRequest,Employee, LeaveType, LeaveCredit, Status, Designation
from .serializers import EmployeeSerializer, LeaveTypeSerializer
from rest_framework import status
import json
from django.http import HttpResponsePermanentRedirect


class BaseSetUp(APITestCase):

	def setUp(self):
		self.client = APIClient()

		software_developer = Designation.objects.create(
								code=1,
								name="Software Developer"
								)
		software_trainee = Designation.objects.create(
								code=2,
								name="software Traineer"
								)
		
		personal = LeaveType.objects.create(
								code=1,
								catagory="Personal"
								)
		
		sick = LeaveType.objects.create(
								code=2, 
								catagory="Sick")
		
		earned = LeaveType.objects.create(
								code=3,
								catagory="Earned"
								)
		
		raveena = Employee.objects.create(
								code=1,
								name="Raveena",
								email="raveena@gmail.com",
								join_date="2018-02-13",
								mode=1,
								designation=software_developer,
								reporting_senior=None
								)

		nagarani = Employee.objects.create(
								code=2,
								name="Nagarani",
								email="nagarani@gmail.com",
								join_date="2018-02-13",
								mode=1,
								designation=software_developer,
								reporting_senior=raveena
								)
		
		nithya = Employee.objects.create(
								code=3,
								name="Nithya",
								email="nithya@gmail.com",
								join_date="2018-02-13",
								mode=1,
								designation=software_developer,
								reporting_senior=raveena
								)

		omprakash = Employee.objects.create(
								code=4, 
								name="OmPrakash", 
								email="om@gmail.com", 
								join_date="2016-05-10", 
								mode=1, 
								designation=software_trainee,
								reporting_senior=raveena
								)
		
		
		prabu = Employee.objects.create(
								code=5, 
								name="Prabu", 
								email="prabu@gmail.com", 
								join_date="2016-04-10", 
								mode=1, 
								designation=software_trainee,
								reporting_senior=nagarani
								)
		
		pending = Status.objects.create(
								code=1,
								status="Pending"
								)

		approved = Status.objects.create(
								code=2,
								status="Approved"
								)
		
		rejected = Status.objects.create(
								code=3,
								status="Rejected"
								)
		
		LeaveRequest.objects.create(
								name=nagarani,
								reporter=nagarani.reporting_senior,
								leave_type=personal,
								from_date="2018-12-12",
								to_date="2018-12-13",
								no_days=2,
								reason="marriage",
								status=pending
								)
		
		LeaveRequest.objects.create(
								name=nithya,
								reporter=nithya.reporting_senior,
								leave_type=personal,
								from_date="2018-12-12",
								to_date="2018-12-13",
								no_days=2,
								reason="marriage",
								status=pending
								)
		LeaveCredit.objects.create(
								name=nagarani,
								leave_type=personal,
								available=11
								)
		LeaveCredit.objects.create(
								name=nagarani,
								leave_type=sick,
								available=11
								)
		LeaveCredit.objects.create(
								name=omprakash,
								leave_type=personal,
								available=11
								)

class EmployeeTest(BaseSetUp):
	
	def test_employee(self):
		# print Employee.objects.all()
		response = self.client.get("http://127.0.0.1:8000/leave/employee/?id=2")	
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_invalid_id(self):
		response = self.client.get("http://127.0.0.1:8000/leave/employee/?id=10")
		self.assertEqual(response.data, "Invalid id")

class LeaveTypeTest(BaseSetUp):

	def test_leave_types(self):
		response = self.client.get("http://127.0.0.1:8000/leave/types/")	
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class  ApplyTest(BaseSetUp):

	def test_apply(self):
		request_data = {
	 					"name": "Nagarani",
						"leave_type": "Personal",
	 					"from_date": "2018-04-17",
	 					"to_date": "2018-04-20",
	 					"reason": "fever"
	 					}
	 	response = self.client.post("http://127.0.0.1:8000/leave/apply/",request_data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_date_format(self):
		request_data = {
	 					"name": "Nagarani",
						"leave_type": "Personal",
	 					"from_date": "2018-04-17",
	 					"to_date": "2018-04-10",
	 					"reason": "fever"
	 					}
		response = self.client.post("http://127.0.0.1:8000/leave/apply/",request_data, format='json')
		self.assertEqual(response.data,"Invalid date")

	def test_from_date(self):
		request_data = {
	 					"name": "Nagarani",
						"leave_type": "Personal",
	 					"from_date": "",
	 					"to_date": "2018-04-10",
	 					"reason": "fever"
	 					}
		response = self.client.post("http://127.0.0.1:8000/leave/apply/",request_data, format='json')
		self.assertEqual(response.data,"Please fill from date")

	def test_to_date(self):
		request_data = {
	 					"name": "Nagarani",
						"leave_type": "Personal",
	 					"from_date": "2018-04-10",
	 					"to_date": "",
	 					"reason": "fever"
	 					}
		response = self.client.post("http://127.0.0.1:8000/leave/apply/",request_data, format='json')
		self.assertEqual(response.data,"Please fill to date")

class ApproveTest(BaseSetUp):

	def test_approve(self):
		data = {
				"request_id": 1,
				"reporter": 2
		}
		response = self.client.put("leave/approve/", data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_invalid_reporter(self):
		data = {
				"request_id": 7,
				"reporter": 2
		}
		response = self.client.put("approve/", data, format='json')
		self.assertEqual(response.data, "DoesNotExist:\n('Employee matching query does not exist.',)")

	def test_invalid_requester(self):
		data = {
				"request_id": 1,
				"reporter": 10
		}
		response = self.client.put("approve/", data, format='json')
		self.assertEqual(response.data, "DoesNotExist:\n('Employee matching query does not exist.',)")

class DenyTest(BaseSetUp):

	def test_deny(self):
		data = {
				"request_id": 1,
				"reporter": 2
		}
		response = self.client.put("leave/deny/", data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_invalid_reporter(self):
		data = {
				"request_id": 7,
				"reporter": 2
		}
		response = self.client.put("leave/deny/", data, format='json')
		self.assertEqual(response.data, "DoesNotExist:\n('Employee matching query does not exist.',)")

class LoginTest(BaseSetUp):

	def test_reporter_login(self):
		response = self.client.put("/leave/login?id=1")
		self.assertEqual(response.data,"{user:reporter}")

	def test_employee_login(self):
		response = self.client.put("/leave/login?id=4")
		self.assertEqual(response.data,"{user:employee}")

	def test_invalid_login(self):
		response = self.client.put("/leave/login?id=0")
		self.assertEqual(response.data,"{user:invalid}")




