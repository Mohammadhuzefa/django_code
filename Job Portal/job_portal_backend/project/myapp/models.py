from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.user.username
 
from django.db import models
from django.contrib.auth.models import User

# 1. Job Postings Table
class Job(models.Model):
    title = models.CharField(max_length=255)
    salary = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# 2. User Profile (Resume ke liye)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)

# 3. Applications Table
class Application(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="apps")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'user') # Ek user ek job pe ek hi baar apply kare
