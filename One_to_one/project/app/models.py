from django.db import models

# Create your models here.
class Aadhar(models.Model):
    aadhar_no=models.IntegerField()
    created_data=models.DateField(auto_now_add=True)
    created_by=models.CharField(max_length=50)

    def __str__(self):
        return str(self.aadhar_no)

class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    city=models.CharField()
    a_no=models.OneToOneField(Aadhar,on_delete=models.CASCADE)