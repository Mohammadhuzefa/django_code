from django.db import models

# Create your models here.
class Student(models.Model):
   
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    pas = models.CharField(max_length=12)

 