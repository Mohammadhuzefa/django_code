# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import StudentSerializer
# from .models import Student
# from django.http import Http404

# # Create your views here.
# @api_view(['GET', 'POST'])
# def stu_list(req):
#     if req.method=='POST':
#         serializer = StudentSerializer(data=req.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     stu = Student.objects.all()
#     serializer = StudentSerializer(stu, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'PUT','PATCH','DELETE'])
# def stu_details(req,pk):
    
# 	u_id = Student.objects.filter(id=pk)
# 	if u_id:
# 		if req.method=='PUT':
# 			snippet = Student.objects.get(id=pk)
# 			serializer = StudentSerializer(snippet, data=req.data)
# 			if serializer.is_valid():
# 				serializer.save()
# 				return Response(serializer.data)
# 			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 		elif req.method=='PATCH':
# 			snippet = Student.objects.get(id=pk)
# 			serializer = StudentSerializer(snippet, data=req.data, partial=True)
# 			if serializer.is_valid():
# 				serializer.save()
# 				return Response(serializer.data)
# 			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 		elif req.method=='DELETE':
# 			snippet = Student.objects.get(id=pk)
# 			snippet.delete()
# 			return Response(status=status.HTTP_204_NO_CONTENT)
		
# 		snippet = Student.objects.get(id=pk)
# 		serializer = StudentSerializer(snippet)
# 		return Response(serializer.data)
# 	else:
# 		return Response({}, status=status.HTTP_400_BAD_REQUEST)
 

from .models import Student
from serializers import StudentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class stu_list(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = Student.objects.all()
        serializer = StudentSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class stu_details(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = StudentSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = StudentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)