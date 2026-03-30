from django.shortcuts import render
from .models import Student,Officer
from django.shortcuts import get_object_or_404
from .serializers import StudentSerializer,OfficerSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


# class UserViewSet(viewsets.ViewSet):
#     """
#     Example empty viewset demonstrating the standard
#     actions that will be handled by a router class.
#     If you're using format suffixes, make sure to also include
#     the `format=None` keyword argument for each action.
#     """

#     def list(self, request):
#         # queryset = Student.objects.all()
#         # serializer = StudentSerializer(queryset, many=True)
#         # return Response(serializer.data)
#         snippets = Student.objects.all()
#         serializer = StudentSerializer(snippets, many=True)
#         return Response(serializer.data)


#     def create(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def retrieve(self, request, pk):
#         xyz=Student.objects.filter(id=pk)
#         if xyz:
#             snippet = Student.objects.get(id=pk)
#             serializer = StudentSerializer(snippet)
#             return Response(serializer.data)
#         else:
#             return Response(
#                 {'error':'not found '},
#                 status=status.HTTP_404_NOT_FOUND
#             )


#     def update(self, request, pk):
#         snippet = Student.objects.get(id=pk)
#         serializer = StudentSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, pk):
#         snippet = Student.objects.get(id=pk)
#         serializer = StudentSerializer(snippet, data=request.data,partial_update=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk):
#         snippet = Student.objects.get(id=pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

 
# model viewset


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class OfficerViewSet(viewsets.ModelViewSet):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer