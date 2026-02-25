from django.db import models


# Create your models here.

class dep(models.Model):
    dept_name=models.CharField(max_length=50,null=True,blank=True)
    dept_code=models.CharField(max_length=50,null=True,blank=True)
    dept_head=models.CharField(max_length=50,null=True,blank=True)
    dept_budget=models.CharField(max_length=50,null=True,blank=True)
    dept_desc=models.CharField(max_length=50,null=True,blank=True)
    dept_emp=models.CharField(max_length=50,null=True,blank=True)


class emp(models.Model):
    fname=models.CharField(max_length=50,null=True,blank=True)
    lname=models.CharField(max_length=50,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    img=models.ImageField()
    adhaar=models.ImageField()
    code=models.CharField(max_length=50,null=True,blank=True)
    mobile=models.CharField(max_length=50,null=True,blank=True)
    DOB=models.CharField(max_length=50,null=True,blank=True)
    gender=models.CharField(max_length=50,null=True,blank=True)
    edu=models.CharField(max_length=50,null=True,blank=True)
    dept=models.CharField(max_length=50,null=True,blank=True)