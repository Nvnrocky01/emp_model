from django.shortcuts import render

# Create your views here.

from app.models import *

def dept(request):
    qsdo=Dept.objects.all()
    d={'dept':qsdo}
    return render(request,'dept.html',d)



def employee(request):
    qseo=Employee.objects.all()
    d={'employee':qseo}
    return render(request,'employee.html',d)



def salgrade(request):
    qsso=Salgrade.objects.all()
    d={'salgrade':qsso}
    return render(request,'salgrade.html',d)


def bonus(request):
    qsbo=Bonus.objects.all()
    d={'bonus':qsbo}
    return render(request,'bonus.html',d)



def insert_dept(request):
    dn=int(input('enter deptno'))
    n=input('enter name')
    dl=input('enter loc')
    do=Dept.objects.get_or_create(dept_no=dn ,dept_name=n,dept_loc=dl)[0]
    do.save()
    return render(request,'dept.html')


def insert_employee(request):
    en=int(input('en'))
    n=input('name')
    es=int(input('salary'))
    ee=input('eamil')
    dn=int(input('dn'))
    do=Dept.objects.get(dept_no=dn)
    eo=Employee.objects.get_or_create(emp_no=en,emp_name=n,emp_salary=es,emp_email=ee,dept_no=do)[0]
    eo.save()
    return render(request,'employee.html')


def insert_salgrade(request):
    es=int(input())
    g=input()
    ls=int(input())
    hs=int(input())
    eo=Employee.objects.get(emp_salary=es)
    so=Salgrade.objects.get_or_create(emp_salary=eo,grade=g,lowsal=ls,highsal=hs)[0]
    so.save()
    return render(request,'salgrade.html')

def insert_bonus(request):
    es=int(input())
    ba=int(input())
    eo=Employee.objects.get(emp_salary=es)
    bo=Salgrade.objects.get_or_create(emp_salary=eo,bonus_amount=ba)[0]
    bo.save()
    return render(request,'bonus.html')

