from django.shortcuts import render
from .models import Employee,Department

# Create your views here.

def landing(req):
  return render(req,'landing.html')

def forword_data(re):
 # first method
 data = Employee.objects.all()
 # print(data.query)
 for i in data:
 
    print(i.name,i.email,i.city,i.mobile,i.course,i.dep_data.d_name,i.dep_data.d_disc) 
 # second method
 data = Employee.objects.select_related('dep_data') # recomended
 # print(data.query)
 for i in data:
 
    print(i.name,i.email,i.city,i.mobile,i.course,i.dep_data.d_name,i.dep_data.d_disc)


def reverse_data(req):
 # first method
 data = Department.objects.all()
 for i in data:
    print(i.d_name,i.d_disc,i.employee_set.all())
 
 # second method
 data = Department.objects.prefetch_related('employee_set')
 for i in data:
    print(i.d_name,i.d_disc,i.employee_set.all()) 