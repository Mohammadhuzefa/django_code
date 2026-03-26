from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics


class Stu_List(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class Stu_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer