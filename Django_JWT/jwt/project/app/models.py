from django.db import models

# Create your models here.
from django.db import models

 

# Create your models here.
roll=(('admin','admin'),('staff','staff'),('user','user'))
class Officer(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    post=models.CharField(max_length=20)
    salary=models.IntegerField()
    roll=models.CharField(choices=roll)

    

 
   