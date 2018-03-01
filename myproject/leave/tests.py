# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.test import APITestCase, APIClient
from . import views
from models import LeaveRequest,Employee, LeaveType, LeaveCredit, Status, Designation
from .serializers import EmployeeSerializer, LeaveTypeSerializer
from rest_framework import status
import json
from django.urls import reverse


class BaseSetUp(APITestCase):
	
	@classmethod
	def setUpClass(cls):

		cls.client = APIClient()

		cls.software_developer = Designation.objects.create(
								code=1,
								name="Software Developer"
								)
		cls.software_trainee = Designation.objects.create(
								code=2,
								name="software Traineer"
								)
		
		cls.personal = LeaveType.objects.create(
								code=1,
								catagory="Personal"
								)
		
		cls.sick = LeaveType.objects.create(
								code=2, 
								catagory="Sick")
		
		cls.earned = LeaveType.objects.create(
								code=3,
								catagory="Earned"
								)
		
		cls.raveena = Employee.objects.create(
								code=1,
								name="Raveena",
								email="raveena@gmail.com",
								join_date="2018-02-13",
								mode=1,
								designation=cls.software_developer,
								reporting_senior=None
								)

		cls.nagarani = Employee.objects.create(
								code=2,
								name="Nagarani",
								email="nagarani@gmail.com",
								join_date="2018-02-13",
								mode=1,
								designation=cls.software_developer,
								reporting_senior=cls.raveena
								)
		
		cls.nithya = Employee.objects.create(
								code=3,
								name="Nithya",
								email="nithya@gmail.com",
								join_date="2018-02-13",
								mode=1,
								designation=cls.software_developer,
								reporting_senior=cls.raveena
								)

		cls.omprakash = Employee.objects.create(
								code=4, 
								name="OmPrakash", 
								email="om@gmail.com", 
								join_date="2016-05-10", 
								mode=1, 
								designation=cls.software_trainee,
								reporting_senior=cls.raveena
								)
		
		
		cls.prabu = Employee.objects.create(
								code=5, 
								name="Prabu", 
								email="prabu@gmail.com", 
								join_date="2016-04-10", 
								mode=1, 
								designation=cls.software_trainee,
								reporting_senior=cls.nagarani
								)
		
		cls.pending = Status.objects.create(
								code=1,
								status="Pending"
								)

		cls.approved = Status.objects.create(
								code=2,
								status="Approved"
								)
		
		cls.rejected = Status.objects.create(
								code=3,
								status="Rejected"
								)
		
		cls.request_one = LeaveRequest.objects.create(
								name=cls.nagarani,
								reporter=cls.nagarani.reporting_senior,
								leave_type=cls.personal,
								from_date="2018-12-12",
								to_date="2018-12-13",
								no_days=2,
								reason="marriage",
								status=cls.pending
								)
		
		cls.request_two = LeaveRequest.objects.create(
								name=cls.nithya,
								reporter=cls.nithya.reporting_senior,
								leave_type=cls.personal,
								from_date="2018-12-12",
								to_date="2018-12-13",
								no_days=2,
								reason="marriage",
								status=cls.pending
								)
		cls.naga_personal = LeaveCredit.objects.create(
								name=cls.nagarani,
								leave_type=cls.personal,
								available=11
								)
		cls.naga_sick = LeaveCredit.objects.create(
								name=cls.nagarani,
								leave_type=cls.sick,
								available=11
								)
		cls.om_peronal = LeaveCredit.objects.create(
								name=cls.omprakash,
								leave_type=cls.personal,
								available=11
								)
	@classmethod
	def tearDownClass(cls):
		cls.software_developer.delete()
		cls.software_trainee.delete()
		cls.personal.delete()
		cls.sick.delete()
		cls.earned.delete()
		cls.raveena.delete()
		cls.nagarani.delete()
		cls.nithya .delete()
		cls.omprakash.delete()
		cls.prabu.delete()
		cls.pending.delete()
		cls.approved.delete()
		cls.rejected.delete()
		cls.request_one.delete()
		cls.request_two.delete()
		cls.naga_personal.delete()
		cls.om_peronal.delete()

class EmployeeTest(BaseSetUp):
	
	def test_employee(cls):
		
		# user_id = cls.Employee.objects.first().id
		response = cls.client.get("/leave/employee/?id={0}".format(cls.raveena.id))
		cls.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_invalid_id(cls):
		response = cls.client.get("/leave/employee/?id={0}".format(30))
		cls.assertEqual(response.data, "Invalid id")

class LeaveTypeTest(BaseSetUp):

	def test_leave_types(cls):
		response = cls.client.get("/leave/types/")	
		cls.assertEqual(response.status_code, status.HTTP_200_OK)

class  ApplyTest(BaseSetUp):

	def test_apply(cls):
		request_data = {
	 					"name": "Nagarani",
						"leave_type": "Personal",
	 					"from_date": "2018-04-17",
	 					"to_date": "2018-04-20",
	 					"reason": "fever"
	 					}
	 	response = cls.client.post("/leave/apply/",request_data, format='json')
		cls.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_date_format(cls):
		request_data = {
	 					"name": "Nagarani",
						"leave_type": "Personal",
	 					"from_date": "2018-04-17",
	 					"to_date": "2018-04-10",
	 					"reason": "fever"
	 					}
		response = cls.client.post("/leave/apply/",request_data, format='json')
		cls.assertEqual(response.data,"Invalid date")

	def test_from_date(cls):
		request_data = {
	 					"name": "Nagarani",
						"leave_type": "Personal",
	 					"from_date": "",
	 					"to_date": "2018-04-10",
	 					"reason": "fever"
	 					}
		response = cls.client.post("/leave/apply/",request_data, format='json')
		cls.assertEqual(response.data,"Please fill from date")

	def test_to_date(cls):
		request_data = {
	 					"name": "Nagarani",
						"leave_type": "Personal",
	 					"from_date": "2018-04-10",
	 					"to_date": "",
	 					"reason": "fever"
	 					}
		response = cls.client.post("/leave/apply/",request_data, format='json')
		cls.assertEqual(response.data,"Please fill to date")

class ApproveTest(BaseSetUp):

	def test_approve(cls):
		data = {
				"reporter_id": 1,
				"request_id": 2
		}
		response = cls.client.put("/leave/approve/", data, format='json')
		cls.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_invalid_reporter(cls):
		data = {
				"reporter_id": 30,
				"request_id": 2
		}
		response = cls.client.put("/leave/approve/", data)
		cls.assertEqual(response.data, "Invalid Id")

	def test_invalid_requester(cls):
		data = {
				"reporter_id": 1,
				"request_id": 40
		}
		response = cls.client.put("/leave/approve/", data, format='json')
		cls.assertEqual(response.data, "Invalid Id")

	def test_wrong_requester(cls):

		data = {
				"reporter_id": 1,
				"request_id": 5
		}
		response = cls.client.put("/leave/approve/", data, format='json')
		cls.assertEqual(response.data, "Invalid Id")

class DenyTest(BaseSetUp):

	def test_deny(cls):
		data = {
				"request_id": 1,
				"reporter": 2
		}
		response = cls.client.put("/leave/deny/", data, format='json')
		cls.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_invalid_reporter(cls):
		data = {
				"reporter_id": 30,
				"request_id": 2
		}
		response = cls.client.put("/leave/deny/", data, format='json')
		cls.assertEqual(response.data, "Invalid Id")

	def test_invalid_requester(cls):
		data = {
				"reporter_id": 1,
				"request_id": 40
		}
		response = cls.client.put("/leave/deny/", data, format='json')
		cls.assertEqual(response.data, "Invalid Id")

	def test_wrong_requester(cls):

		data = {
				"reporter_id": 1,
				"request_id": 5
		}
		response = cls.client.put("/leave/deny/", data, format='json')
		cls.assertEqual(response.data, "Invalid Id")


class DetailTest(BaseSetUp):

	def test_details(cls):
		response = cls.client.get("/leave/details/?format=json&&id=2")
		cls.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_invalid_id(cls):
		response = cls.client.get("/leave/details/?format=json&&id=10")
		cls.assertEqual(response.data, "Invalid id")

class LeaveBalanceTest(BaseSetUp):

	def test_balance(cls):
		response = cls.client.get("/leave/availables/?format=json&id=1")
		cls.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_invalid_id(cls):
		response = cls.client.get("/leave/availables/?format=json&id=10")
		cls.assertEqual(response.data, "Invalid id")

class LoginTest(BaseSetUp):

	def test_reporter_login(cls):
		response = cls.client.get("/leave/login/?format=json&id=1")
		cls.assertEqual(response.data,"{user:reporter}")

	def test_employee_login(cls):
		response = cls.client.get("/leave/login/?format=json&id=4")
		cls.assertEqual(response.data,"{user:employee}")

	def test_invalid_login(cls):
		response = cls.client.get("/leave/login/?format=json&id=0")
		cls.assertEqual(response.data,"{u'user': u'invalid'}")

