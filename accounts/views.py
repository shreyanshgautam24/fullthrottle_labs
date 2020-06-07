# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from rest_framework.response import Response
from .models import *
from django.http import JsonResponse
import json
# Create your views here.
class fullthrottleAPIView(APIView):
    renderer_classes = (JSONRenderer,)
    def get(self , request , format = None):
        members = []
        all_users= User.objects.all()
        for i in all_users:
            user_activity = ActivityPeriod.objects.filter(user = i)
            actarr = []
            members.append({"id" : i.real_id,"real_name":i.real_name,"tz":i.time_zone,"activity_periods": actarr})
            for j in user_activity.values('start_time','end_time'):
                actarr.append(j)
            # myDate.strftime("%Y-%m-%d %H:%M:%S")
        return Response( {'ok':'true','members':members}  )
