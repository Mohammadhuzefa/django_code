from django.db import models

# Create your models here.

class data(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    contact=models.CharField(max_length=20)
    age=models.IntegerField()


