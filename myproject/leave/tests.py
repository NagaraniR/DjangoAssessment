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
		
		self.designation = Designation.objects.create(
								code=1,
								name="Software Developer"
								)
		
		self.leave_type_personal = LeaveType.objects.create(
								code=1,
								catagory="Personal"
								)
		
		self.leave_type_sick = LeaveType.objects.create(
								code=2, 
								catagory="Sick")
		
		self.leave_type_earned = LeaveType.objects.create(
								code=3,
								catagory="Earned"
								)
		
		self.raveena = Employee.objects.create(
										code=1,
										name="Raveena",
										email="raveena@gmail.com",
										join_date="2018-02-13",
										mode=1,
										designation=self.designation,
										reporting_senior=None
										)

		self.nagarani = Employee.objects.create(
								code=2,
								name="Nagarani",
								email="nagarani@gmail.com",
								join_date="2018-02-13",
								mode=1,
								designation=self.designation,
								reporting_senior=self.raveena
								)
		
		self.nithya = Employee.objects.create(
								code=3,
								name="Nithya",
								email="nithya@gmail.com",
								join_date="2018-02-13",
								mode=1,
								designation=self.designation,
								reporting_senior=self.raveena
								)

		self.omprakash = Employee.objects.create(
								code=1000, 
								name="OmPrakash", 
								email="om@gmail.com", 
								join_date="2016-05-10", 
								mode=1, 
								designation=self.designation,
								reporting_senior=self.prabu
								)
		
		self.prabu = Employee.objects.create(
								code=1001, 
								name="Prabu", 
								email="prabu@gmail.com", 
								join_date="2016-04-10", 
								mode=1, 
								designation=self.designation,
								reporting_senior=self.omprakash
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
									name=self.nagarani,
									reporter=self.nagarani.reporting_senior,
									leave_type=self.leave_type_sick,
									from_date="2018-12-12",
									to_date="2018-12-13",
									no_days=2,
									reason="marriage",
									status=Status.objects.get(id=1)
									)
		
		LeaveRequest.objects.create(
									name=self.nithya,
									reporter=self.nithya.reporting_senior,
									leave_type=self.leave_type_earned,
									from_date="2018-12-12",
									to_date="2018-12-13",
									no_days=2,
									reason="marriage",
									status=Status.objects.get(id=2)
									)
		LeaveCredit.objects.create(
					            name=self.nagarani,
					            leave_type = LeaveType.objects.get(id=1),
					            available="3"
					            )

        LeaveCredit.objects.create(
								name=self.omprakash,
								leave_type = LeaveType.objects.get(id=1),
								available="3"
								)

    # # Test leave approval
    # def test_approve(self):
    # 	response = self.client.put(
    # 		'http://127.0.0.1:8000/leave/deny/', {"id": 1}, format='json'
    # 		)
    #     self.assertEqual(response.status_code, 200)

    # #Test wrong url
    # def test_worng_url_approve(self):
    # 	response = self.client.put(
    # 		'http://127.0.0.1:8000/leave/approved/', {"id": 1}, format='json'
    # 		)
    #     self.assertEqual(response.status_code, 404)

    # #Test wrong data
    # def test_wrong_data_approve(self):
    # 	response = self.client.get(
    # 		'http://127.0.0.1:8000/leave/approve/', { "id": 1, "status":"Approved" }, format='json'
    # 		)
    #     self.assertEqual(response.status_code, 200)

    # def test_unexist_id(self):
    # 	response = self.client.get(
    # 		'http://127.0.0.1:8000/leave/approve/', {"id": 0}, format='json'
    # 		)
    #     self.assertEqual(response.status_code, 405)

class ApplyGetTestCase(BaseSetUp):
	
	def test_user_data(self):
		response = self.client.get("http://127.0.0.1:8000/leave/apply/employee/2/")	
		employee_serializer = EmployeeSerializer(Employee.objects.filter(id=1), many=True)
		leave_serializer = LeaveTypeSerializer(LeaveType.objects.all(), many=True)
		expected = {"employee":employee_serializer.data, "leave_types":leave_serializer.data}
		if response.data is not None:
			self.assertEqual(response.data, expected)
		else:
			self.assertIs(response.data, None)

	def test_response_bad_request(self):
		response = self.client.get("http://127.0.0.1:8000/leave/apply/employee/3/")			
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
		self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

	def test_request_not_found(self):
		response = self.client.get("http://127.0.0.1:8000/WAPPR/6/", format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class LeaveApplicationTest(BaseSetUp):
	# Test leave approval
    def test_approve(self):
        response = self.client.put('http://127.0.0.1:8000/leave/deny/', {"id": 1}, 
        	format='json')
        self.assertEqual(response.status_code, 200)

    #Test wrong url
    def test_worng_url_approve(self):
    	response = self.client.put('http://127.0.0.1:8000/leave/approved/', {"id": 1}, 
        	format='json')
        self.assertEqual(response.status_code, 404)

    #Test wrong data
    def test_wrong_data_approve(self):
    	response = self.client.get('http://127.0.0.1:8000/leave/approve/', 
    		{
    		"id": 1, 
    		"status":"Approved"
    		}, 
        	format='json')
        self.assertEqual(response.status_code, 200)

    def test_unexist_id(self):
    	response = self.client.get('http://127.0.0.1:8000/leave/approve/', {"id": 0}, 
        	format='json')
        self.assertEqual(response.status_code, 405)

class  LeaveBalanceTest(BaseSetUp):

	def test_leave_balance(self):
		response = self.client.get('http://127.0.0.1:8000/leave/available/2/', format='json')
    	self.assertEqual(response.data, 405)

	def test_badurl_leave_balance(self):
		response = self.client.get('http://127.0.0.1:8000/leave/avail/0/', format='json')
    	self.assertEqual(response.data, 200)