"""
URL configuration for project21 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dept/',dept,name='dept'),
    path('employee/',employee,name='employee'),
    path('salgrade/',salgrade,name='salgrade'),
    path('bonus/',bonus,name='bonus'),
    path('insert_dept/',insert_dept,name='insert_dept'),
    path('insert_employee/',insert_employee,name='insert_employee'),
    path('insert_salgrade/',insert_salgrade,name='insert_salegrade'),
     path('insert_bonus/',insert_bonus,name='insert_bonus'),
]




