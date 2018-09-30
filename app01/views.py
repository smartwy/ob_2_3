from django.shortcuts import render

# Create your views here.

#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Name:
#Descripton:
#Author:    smartwy
#Date:
#Version:
from django.shortcuts import render,HttpResponse
from django.views import View
import os

USER_DICT = {
	'id-1':{'name':'root1','email':'abc@163.com'},
	'id-2':{'name':'root2','email':'abc@163.com'},
	'id-3':{'name':'root3','email':'abc@163.com'},
	'id-4':{'name':'root4','email':'abc@163.com'},
}

def detail(request, **kwargs):  # 使用关键字参数，使用实参名作为Key值调用

	info = USER_DICT[kwargs['reg']+'-'+kwargs['arg']]
	return render(request, 'detail.html',{'info': info})

def index(request):

	print(request.path_info)# 打印当前请求的url
	return render(request, 'index.html', {'user_dict': USER_DICT})
