from django.db import models

# Create your models here.

class Data(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    contact=models.IntegerField()
    age=models.IntegerField()

    