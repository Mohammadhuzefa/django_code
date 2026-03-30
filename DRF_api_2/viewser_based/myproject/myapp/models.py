from django.db import models

 
 
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    contact=models.CharField(max_length=20)
    age=models.IntegerField()

class Officer(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    post=models.CharField(max_length=20)
    salary=models.IntegerField()
