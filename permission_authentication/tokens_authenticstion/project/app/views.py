from django.shortcuts import render
from .models import Officer
from django.shortcuts import get_object_or_404
from .serializers import OfficerSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

class OfficerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Officer.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication] objectt lvel 
    serializer_class = OfficerSerializer