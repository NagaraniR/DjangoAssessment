# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response

# <<<<<<< HEAD
# from models import Designation, Employee, Status, LeaveType, LeaveCredit, LeaveRequest
# from serializers import UserSerializer, LeaveRequestSerializer, LeaveCreditSerializer, StatusSerializer
# =======
# from models import Designation, User, Status, LeaveType, LeaveCredit, LeaveRequest

# from serializers import UserSerializer, LeaveRequestSerializer, LeaveCreditSerializer, StatusSerializer, LeaveRequestSerializer2

# >>>>>>> bc86fafb300efa29b19f7206ca117bc6ae4ff3be

from models import Status, LeaveRequest
from django.core.serializers.python import Serializer
#from serializers import UserSerializer
from rest_framework.response import Response
from .serializers import createSerializer
# from rest_framework.generics import CreateAPIView

# import requests


#class LeaveApproval(APIView):
    

# Create your views here.
class ApplyView(APIView):
    
    def post(self, request, format=None):
        #import pdb;pdb.set_trace()
        status = Status.objects.get(code=101)
        data = request.data 
        data["status"]= status.id
        serializer = createSerializer(data=data, many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ApplyView(APIView)
class Approve(APIView):

    def get_leaves(self, pk):
        try:
            return LeaveRequest.objects.get(id=pk)
        except LeaveRequest.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_leaves(pk)
        user = createSerializer(user)
        return Response(user.data)

    def put(self,request, pk, format=None):
        user = self.get_leaves(pk)
        status = Status.objects.get(status=request.data["status"])
        request.data["status"] = status.status
        serializer = createSerializer(request.data, many=False) 
        if serializer.is_valid(raise_exception=True):
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors)

        # user = LeaveRequest.objects.get(id=request.data["id"])
        # status = Status.objects.get(status=request.data["status"])
        # user.status = status
        # user.save()
        # serializer = createSerializer(user)
        # return Response(serializer.data)
        
        # import pdb;pdb.set_trace()
        # status = Status.objects.get(status=request.data["status"])
        # request.data["status"] = status.id
        # serializer = updateSerializer(request.data,)
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        # return Response(serializer.data) 
        # return Response(status=status.HTTP_404_NOT_FOUND)



        # code = request.GET.get('code')
        # employee = Employee.objects.get(code=code)
        # status = Status.objects.get(code=100)
        # if employee:
        #     data = request.data
        #     data["status"] = status.id
        #     serializer = createSerializer(data=data, many=False)
        #     if serializer.is_valid(raise_exception=True):
        #         serializer.save()
        #     return Response(serializer.data)
        # return Response(status=status.HTTP_404_NOT_FOUND)













# class Post(APIView):

#     def post(self, request):    
#         # response = requests.get(request.data)
#         # json_data = json.loads(response.text)
#         #value = request.data.encode("utf-8")
#         name = request.data["name"]

#         reporting_senior = request.data["reporting_senior"]
#         credits = request.data["credits"]
#         fromDate = request.data["fromDate"]
#         toDate = request.data["toDate"]
#         reason = request.data["reason"]
#         days = request.data["days"]
#         status = request.data["status"]
#         leave_request = LeaveRequest.objects.create(
#             employee_name= User.objects.get(name=name),
#             reporter = User.objects.get(name=reporting_senior), 
#             leave_type = LeaveType.objects.get(id=credits),
#             from_date = fromDate,
#             to_date = toDate,
#             no_days = days ,
#             reason = reason,
#             status = Status.objects.get(id=status)
#             )
# <<<<<<< HEAD
#         leave_request.save()
#         return Response("returned")

# =======
# >>>>>>> bc86fafb300efa29b19f7206ca117bc6ae4ff3be

#         leave_request.save()
#         return Response("returned")
#         values = json.loads(request.body)
#         # name = data.get("name")
#         print "sdff";
#         user = User.objects.all()
#         return Response(User)

# ##For Approval  
# class ApprovalForm(APIView):


#     def get(self, request, id):
#         user = LeaveRequest.objects.filter(id=id)
#         user = LeaveRequestSerializer(user, many=True)

#     def get(self, request, employee_name):
#         user = LeaveRequest.objects.filter(employee_name__name=employee_name)
#         user = LeaveRequestSerializer(user, many=True)

#         return Response(user.data)

#     def put(self, request, employee_name):
#         user = LeaveRequest.objects.filter(employee_name__name=employee_name)
#         status = Status.objects.get(status=request.data["status"])
#         serializer = LeaveRequestSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class WaitngForApprovalView(APIView):
#     def get(self,request):
#         user = LeaveRequest.objects.all()
#         pending_user = LeaveRequestSerializer(user, many=True)
#         return Response(pending_user.data) 

# class UserView(APIView):
#     def get(self, request, employee_name):
#         #import pdb;pdb.set_trace()
#         user = User.objects.filter(name=employee_name)
#         user_serializer = UserSerializer(user, many=True)
#         return Response(user_serializer.data)

# class LeaveCreditView(APIView):
#     def get(self, request, employee_name):
#         credits = LeaveCredit.objects.filter(user_name__name=employee_name)
#         credit_serializer = LeaveCreditSerializer(credits, many=True )
#         return Response(credit_serializer.data)

# class StatusView(APIView):
#     def get(self, request):
#         status = Status.objects.all()
#         status_serializer = StatusSerializer(status, many=True)
#         return Response(status_serializer.data)

# class LeaveRequestView(APIView):

#     def get(self,request):        
#         leave_request = LeaveRequest.objects.all()
#         leave_request_serializer = LeaveRequestSerializer2(status, many=True)
#         return Response(leave_request_serializer.data)

# @api_view(['GET', 'POST'])
# def apply_leave(self, request):
#     return

    	#import pdb;pdb.set_trace()
    	# user = User.objects.filter(name=employee_name)
    	# 
      #  credits = LeaveCredit.objects.filter(user_name__name=employee_name)
     #    user_serializer = UserSerializer(user, many=True)
     #    credit_serializer = LeaveCreditSerializer(credits, many=True )
     #    user_data = JSONRenderer().render(user_serializer.data)
     #    name_info=json.loads(user_data)
     #    credits_data = JSONRenderer().render(credit_serializer.data)
     #    leave_credit=json.loads(credits_data)
     #    return Response({'user_data': name_info, 'credits_data':leave_credit}, template_name='leave/apply.html')

# class ApplyForm(generics.ListCreateAPIView):

# 	#def get(self, request)
# 	#@api_view(['GET'])
# 	def list(self, request, employee_name):
# 		queryset_one = User.objects.filter(name = employee_name)
# 		user_serializer = UserSerializer(queryset_one, many=True)
# 		return Response(user_serializer.data)


	# def getCredits(self, request, employee_name):	
	#     queryset_two = LeaveCredit.objects.filter(user_name__name = employee_name)
	#     leave_credit_serializer = LeaveCreditSerializer(queryset_two, many=True)
	#     return JsonResponse(leave_credit_serializer.data, safe=False)
    # @api_view(['GET', 'POST', 'PUT', 'DELETE'])	
    # #@renderer_classes((JSONRenderer,))
    # def person_list(request, employee_name):
    #     if request.method == 'GET':
    #         #email = request.GET.get('email')
    #         if employee_name:
    #             user = User.objects.filter(name=employee_name)
    #         # else:
    #         #     user = User.objects.all()
    #         serializer = UserSerializer(user, many=True)
    #         data = serializer.data
    #         return Response({'user_data':data},apply.html)
