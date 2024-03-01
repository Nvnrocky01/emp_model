from django.db import models

# Create your models here.

class Dept(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=100,unique=True)
    dept_loc=models.CharField(max_length=100)
    def __str__(self):
        return self.dept_name

class Employee(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=100)
    emp_salary=models.IntegerField(default=5000)
    emp_email=models.EmailField(null=True,default='nvn@email.com')
    dept_no=models.OneToOneField(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.emp_name 

class Salgrade(models.Model):
    emp_salary=models.OneToOneField(Employee,on_delete=models.CASCADE)
    grade=models.IntegerField(null=True,default='A')
    lowsal=models.IntegerField()
    highsal=models.IntegerField()

class Bonus(models.Model):
    emp_salary=models.OneToOneField(Employee,on_delete=models.CASCADE)
    bonus_amount=models.IntegerField()



