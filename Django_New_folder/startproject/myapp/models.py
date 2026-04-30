from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

# class Mobile(models.Model):
#     country_code=models.CharField(max_length=2000)
#     created_at=models.DateField(auto_now_add=True)
#     phone_no=models.IntegerField()

#     def __str__(self):
#         return str(self.phone_no)


# class Caller(models.Model):
#     name=models.CharField(max_length=20)
#     email=models.CharField(max_length=20)
#     city=models.CharField(max_length=20)
#     mobile=models.OneToOneField(Mobile,on_delete=models.CASCADE,related_name='c')


# many many


class car(models.Model):
    country_code=models.CharField(max_length=2000)
    created_at=models.DateField(auto_now_add=True)
    phone_no=models.IntegerField()

    def __str__(self):
        return str(self.phone_no)


class fuel(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    mobile=models.ManyToManyField(car,related_name='c')



    



