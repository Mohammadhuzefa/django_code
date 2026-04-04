from django.db import models
# Create your models here.
class Student(models.Models):
    name=models.CharField()
    email=models.EmailField()
    age=models.IntegerField()
    city=models.CharField()

