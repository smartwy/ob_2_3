"""ob_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from ob_2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.root), # 如果使用url做根映射，会一直在返回hello中
    url(r'^hello/', include('app02.urls')), # FBV 模式
    url(r'^index/', include('app01.urls')), # 内含CBV模式

]
