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

	# def tearDown(self):
 #        del self.a

class ApplyGetTestCase(BaseSetUp):
	
	def test_user_data(self):
		response = self.client.get("http://127.0.0.1:8000/leave/user/apply/2/")	
		employee_serializer = EmployeeSerializer(Employee.objects.filter(id=1), many=True)
		leave_serializer = LeaveTypeSerializer(LeaveType.objects.all(), many=True)
		expected = {"employee":employee_serializer.data, "leave_types":leave_serializer.data}
		self.assertEqual(response.data, expected)

	def test_response_bad_request(self):
		response = self.client.get("http://127.0.0.1:8000/leave/user/apply/3/")			
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
	 					"reason": "fever"
	 					}
	 	self.response = self.client.post("http://127.0.0.1:8000/leave/apply/",request_data, format='json')
		self.assertEqual(self.response.status_code, status.HTTP_200_OK)

	def test_request_not_found(self):
		request_data = {
	 					"name": "Nagarani",
						"leave_type": "Personal",
	 					"from_date": "2018-04-17",
	 					"to_date": "2018-04-20",
	 					"reason": "fever"
	 					}
	 	response = self.client.post("http://127.0.0.1:8000/apply/",request_data, format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_response_format(self):
		request_data = {
	 					"name": "Nagarani",
						"leave_type": "Personal",
	 					"from_date": "2018-04-17",
	 					"to_date": "2018-04",
	 					"reason": "fever"
	 					}
	 	response = self.client.post("http://127.0.0.1:8000/leave/apply/",request_data, format='json')
		self.assertNotEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class LeaveHistoryTestCase(BaseSetUp):

	def test_user_history(self):
		response = self.client.get("http://127.0.0.1:8000/leave/user/history/2/", format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_unknown_id(self):
		response = self.client.get("http://127.0.0.1:8000/leave/user/history/20", format='json')
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

class LeaveApprovalTest(BaseSetUp):
	# Test leave approval
    def test_approve(self):
        response = self.client.put('http://127.0.0.1:8000/leave/deny/', {"id": 1}, 
        	format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #Test wrong url
    def test_worng_url_approve(self):
    	response = self.client.put('http://127.0.0.1:8000/leave/approved/', {"id": 1}, 
        	format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    #Test wrong data
    def test_wrong_data_approve(self):
    	response = self.client.get('http://127.0.0.1:8000/leave/approve/', 
    		{
    		"id": 1, 
    		"status":"Approved"
    		}, 
        	format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_unexist_id(self):
    	response = self.client.get('http://127.0.0.1:8000/leave/approve/', {"id": 0}, 
        	format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

class  LeaveBalanceTest(BaseSetUp):

	def test_leave_balance(self):
		response = self.client.get('http://127.0.0.1:8000/leave/available/57/', format='json')
		self.assertEqual(response.content, '{"Leave available":[{"id":34,"available":11,"name":57,"leave_type":34},{"id":35,"available":11,"name":57,"leave_type":35}]}')

	def test_badurl_leave_balance(self):
		response = self.client.get('http://127.0.0.1:8000/leave/avail/0/', format='json')
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
		
