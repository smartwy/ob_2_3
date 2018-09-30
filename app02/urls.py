#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app02 import views
urlpatterns = [
	path('', views.hello),  # FBV 模式
	url(r'^login', views.Login.as_view()),  # CBV 模式 自动判断请求模式，

]



