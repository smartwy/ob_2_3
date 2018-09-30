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
from app01 import views

urlpatterns = [
    url(r'', views.index, name='index'),
    url(r'^detail-(?P<reg>\w{2,})-(?P<arg>\d+).html', views.detail),  # 正则绑定关联函数的形参名,绑定后形参名对位置不作要求，
]
