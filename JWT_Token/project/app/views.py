from django.shortcuts import render
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from .models import Employee
from rest_framework.permissions import IsAuthenticated



# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    permission_classes = [IsAuthenticated]

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()