from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField()
    Contact=models.BigIntegerField()
    Education=models.CharField(max_length=20)
    City=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    Image=models.ImageField(upload_to='images/')
    Document=models.FileField(upload_to='documents')
    Audio=models.FileField(upload_to='audios')
    Video=models.FileField(upload_to='videos')

    def __str__(self):
        return self.Name + " " +self.Email + " " + str(self.Contact)