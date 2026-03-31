from django.db import models

# Create your models here.

class emp(models.Model):
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    edu = models.CharField(max_length=50, null=True, blank=True)
 


 
