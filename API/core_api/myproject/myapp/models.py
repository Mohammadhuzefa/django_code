from django.db import models

# Create your models here.
class Stu(models.Model):
    name=models.CharField(null=True,max_length=20)
    email=models.CharField(null=True,max_length=20)
    city=models.CharField(null=True,max_length=20)
    age=models.IntegerField(null=True)



