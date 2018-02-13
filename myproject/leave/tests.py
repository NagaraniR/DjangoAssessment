# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.test import APITestCase, APIClient
from . import views
from models import LeaveRequest,Employee, LeaveType, LeaveCredit, Status,Designation
from .serializers import EmployeeSerializer, LeaveTypeSerializer
from rest_framework import status
import json
from django.http import HttpResponsePermanentRedirect


class BaseSetUp(APITestCase):

	def setUp(self):
		self.client = APIClient()
		Designation.objects.create(
								code=1,
								name="Software Developer"
								)
		designation = Designation.objects.get(id=1)
		raveena = Employee.objects.create(
										code=1,
										name="Raveena",
										email="raveena@gmail.com",
										join_date="2018-02-13",
										mode=1,
										designation=designation,
										reporting_senior=None
										)
		LeaveType.objects.create(
								code=1,
								catagory="Personal"
								)
		LeaveType.objects.create(
							code=2,
							catagory="Sick"
							)
		LeaveType.objects.create(
								code=3,
								catagory="Earned"
								)

		nagarani = Employee.objects.create(
								code=2,
								name="Nagarani",
								email="nagarani@gmail.com",
								join_date="2018-02-13",
								mode=1,
								designation=designation,
								reporting_senior=raveena
								)
		nithya = Employee.objects.create(
								code=3,
								name="Nithya",
								email="nithya@gmail.com",
								join_date="2018-02-13",
								mode=1,
								designation=designation,
								reporting_senior=raveena
								
			)
		Status.objects.create(
							code=1,
							status="Pending"
							)
		Status.objects.create(
							code=2,
							status="Approved"
							)
		Status.objects.create(
							code=3,
							status="Rejected"
							)
		LeaveRequest.objects.create(
									name=nagarani,
									reporter=nagarani.reporting_senior,
									leave_type=LeaveType.objects.get(id=1),
									from_date="2018-12-12",
									to_date="2018-12-13",
									no_days=2,
									reason="marriage",
									status=Status.objects.get(id=1)
									)
		LeaveRequest.objects.create(
									name=nithya,
									reporter=nithya.reporting_senior,
									leave_type=LeaveType.objects.get(id=1),
									from_date="2018-12-12",
									to_date="2018-12-13",
									no_days=2,
									reason="marriage",
									status=Status.objects.get(id=2)
									)
			
		
																			

class ApplyGetTestCase(BaseSetUp):

	
	def test_user_data(self):
		
		response = self.client.get("http://127.0.0.1:8000/leave/user/leave/apply/employee/1/")	
		employee_serializer = EmployeeSerializer(Employee.objects.filter(id=1), many=True)
		leave_serializer = LeaveTypeSerializer(LeaveType.objects.all(), many=True)
		expected = {"employee":employee_serializer.data, "leave_types":leave_serializer.data}
		self.assertEqual(response.data, expected)

	def test_response_bad_request(self):
		response = self.client.get("http://127.0.0.1:8000/leave/user/leave/apply/employee/3/")			
		self.assertNotEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_request_not_found(self):	
		response = self.client.get("http://127.0.0.1:8000/leave/applmployee/2/")	
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
		
class ApplyPostTestCase(BaseSetUp):	
	
	def test_post_leave_response(self):
		request_data = {
	 					"name": "Nagarani",
						"leave_type": "Personal",
	 					"from_date": "2018-04-17",
	 					"to_date": "2018-04-20",
	 					"reason": "fever",
	 					"status": "Pending"
	 					}
		
	 	self.response = self.client.post("http://127.0.0.1:8000/leave/apply/",request_data, format='json')
		self.assertEqual(self.response.status_code, status.HTTP_200_OK)

	def test_request_not_found(self):
		request_data = {
	 					"name": "Nagarani",
						"leave_type": "Personal",
	 					"from_date": "2018-04-17",
	 					"to_date": "2018-04-20",
	 					"reason": "fever",
	 					"status": "Pending"
	 					}
		
	 	response = self.client.post("http://127.0.0.1:8000/apply/",request_data, format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_response_format(self):
		request_data = {
	 					"name": "Nagarani",
						"leave_type": "Personal",
	 					"from_date": "2018-04-17",
	 					"to_date": "2018-04",
	 					"reason": "fever",
	 					"status": "Pending"
	 					}
		
	 	response = self.client.post("http://127.0.0.1:8000/leave/apply/",request_data, format='json')
		self.assertNotEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class LeaveHistoryTestCase(BaseSetUp):

	def test_user_history(self):
		response = self.client.get("http://127.0.0.1:8000/leave/user/leave/history/2/", format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_unknown_id(self):
		response = self.client.get("http://127.0.0.1:8000/leave/user/leave/history/20", format='json')
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

	def test_request_not_found(self):
		response = self.client.get("http://127.0.0.1:8000/leave/user/leave/history=h/20", format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class ReportingSeniorsRequestsTestCase(BaseSetUp):

	def test_ReportingSeniors_requests(self):
		response = self.client.get("http://127.0.0.1:8000/leave/WAPPR/1/", format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_unknown_id(self):
		response = self.client.get("http://127.0.0.1:8000/leave/WAPPR/10/", format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_request_not_found(self):
		response = self.client.get("http://127.0.0.1:8000/WAPPR/6/", format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)








		
