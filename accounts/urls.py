from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^fullthrottle_test/$' , fullthrottleAPIView.as_view() ),
]
