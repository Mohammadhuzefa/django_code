from rest_framework import serializers
from .models import EmployeeProfile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class EmployeeProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer() # User ki details bhi sath mein aayengi
    class Meta:
        model = EmployeeProfile
        fields = '__all__'


from rest_framework import serializers
from .models import Job, Application, UserProfile
from django.contrib.auth.models import User

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    job_title = serializers.ReadOnlyField(source='job.title')
    user_name = serializers.ReadOnlyField(source='user.username')
    salary = serializers.ReadOnlyField(source='job.salary')

    class Meta:
        model = Application
        fields = ['id', 'job', 'job_title', 'user', 'user_name', 'salary', 'status', 'applied_at']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['resume']