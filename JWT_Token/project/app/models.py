from django.db import models

# Create your models here.
role=(('admin','admin'),('staff','staff'),('user','user'))

class Employee(models.Model):
    emp_name=models.CharField(max_length=50)
    emp_email=models.EmailField()
    emp_department=models.CharField(max_length=50)
    emp_role=models.CharField(max_length=50,choices=role)