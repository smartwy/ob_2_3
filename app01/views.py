from django.shortcuts import render

# Create your views here.

#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Name:
#Descripton:
#Author:    smartwy
#Date:
#Version:
from django.shortcuts import render
from django.views import View
import os
def hello(request):
	# print('hello')
	return render(request, 'hello.html')

def file_save(request):
	obj = request.FILES.get('filename')  # FILES只取上传的文件
	file_path = os.path.join('upload', obj.name)
	f = open(file_path, mode='wb')
	for i in obj.chunks():
		f.write(i)
	f.close()

class Login(View):
	'''CBV模型中url.py匹配到类时会先执行View的dispatch函数获取请求方法
		也可在自定义类中自定义dispatch函数，优先级高与View中的函数
	'''
	def dispatch(self, request, *args, **kwargs):
		# 调用父类中的dispatch，结果需要在自定义函数内返回
		print('start View.dispatch') # 可以健壮dispatch函数功能，可以理解为装饰器
		result = super(Login, self).dispatch(request, *args, **kwargs)
		print('stop View.dispatch')
		return result

	def post(self,request):
		print('post')
		if request.POST.get('user') == 'asdf' and request.POST.get('passwd') == '123':
			print(request.POST.getlist('fover'),request.POST.get('city')) # getlist 可获取chechbox的多选值
			# 保存上传的文件
			if request.FILES.get('filename'):
				file_save(request)
			return render(request,'loginok.html',{'user':request.POST.get('user'),
			                                      'sex':request.POST.get('gender'),
			                                      'city':request.POST.get('city')})
		else:
			return render(request,'hello.html')
	def get(self,request):
		print('get')
		return render(request, 'hello.html')