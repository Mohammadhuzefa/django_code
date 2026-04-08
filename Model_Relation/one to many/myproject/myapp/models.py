from django.db import models

# Create your models here.
class Department(models.Model):
    d_name = models.CharField(max_length=50)
    d_disc = models.TextField()
    def __str__(self):
        return self.d_name
class Employee(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=50)
    dep_data = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='puju')
    def __str__(self):
        return self.name