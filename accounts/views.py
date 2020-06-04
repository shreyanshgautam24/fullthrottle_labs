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
            user_activity = i.activityUser.all()
            actarr = []
            for j in user_activity.values('start_time','end_time'):
                actarr.append(j)
                members.append({"id" : i.real_id,"real_name":i.real_name,"tz":i.time_zone,"activity_periods": actarr})
            # myDate.strftime("%Y-%m-%d %H:%M:%S")



        return Response( {'ok':'true','members':members}  )

# toReturn[uielem.target] = { "name" : grp.name , "pk" : grp.pk , "desc" : grp.discription , "parent": []}
#                         for x in grp.parent.all():
#                             toReturn[uielem.target]["parent"].append({'pk':x.pk,'link':str(x.link),'attachment':str(x.attachment),'user':x.user.pk,'mediaType':x.mediaType,'imageIndex':x.imageIndex,'title':x.title,'discription':x.discription})
