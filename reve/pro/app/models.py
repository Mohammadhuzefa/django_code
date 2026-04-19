from django.db import models

# Create your models here.
class Student(models.Model):
   name=models.EmailField()
   email=models.CharField(max_length=10)
   contact = models.IntegerField()
   password = models.CharField(max_length=20)