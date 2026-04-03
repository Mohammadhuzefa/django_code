from django.db import models

# Create your models here.



class Patient(models.Model):
    n = models.CharField(max_length=50)
    a = models.IntegerField()
    g = models.CharField(max_length=20)
    m = models.CharField(max_length=15)   
    e = models.EmailField(max_length=50)
    d = models.CharField(max_length=50)
    da = models.DateField()

    def __str__(self):
        return self.n