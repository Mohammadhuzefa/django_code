print("viewa page call")
from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
import csv
from django.urls import reverse
from urllib.parse import urlencode

# Create your views here.
# def landingpage(req):
#     # return HttpResponse("Hello this is first django project")
#     return HttpResponse("<h1 style='color:red;'>Hello this is first django project</h1>")

# def json_response(request):
#   data = {"name": "Neeraj", "role": "Developer"}
#   json_data = json.dumps(data)
#   return HttpResponse(json_data,content_type="application/json")

# def download_csv(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="employees.csv"'
#     writer = csv.writer(response)
#     writer.writerow(['Name', 'Department', 'Salary'])
#     writer.writerow(['Neeraj', 'IT', 50000])
#     writer.writerow(['Ravi', 'HR', 40000])
#     return response

def my_redirect1(req):
   url=reverse('my_redirect2')
   data=urlencode({'name':'Neeraj','age':37})
   return redirect(f'{url}?{data}')

def my_redirect2(req):
  print("hello")
  print(req.method)
  print(req.GET)