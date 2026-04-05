from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title
class Student(models.Model):
    name = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course,related_name='puju')   # M2M relation
    def __str__(self):
        return self.name