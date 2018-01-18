# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from models import Employee, LeaveForm
from serializers import UserLeave
from django.http import HttpResponse, JsonResponse

#class LeaveList(APIView):

def get(request):
	query = LeaveForm.objects.all()
	serializer = UserLeave(query, many=True)
	#return JsonResponse(serializer.data, safe=False)
