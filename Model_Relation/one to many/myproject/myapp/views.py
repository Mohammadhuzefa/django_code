from django.shortcuts import render
from .models import Employee,Department
# Create your views here.
def forword_data(req):
    # data=Employee.objects.all()
    data=Employee.objects.select_related('dep_data')
    return render(req,'forword_data.html',{'data':data})

def reverse_data(req):
    # data=Department.objects.all()
    data=Department.objects.prefetch_related('puju')
    return render(req,'reverse_data.html',{'data':data})


def landing(req):
     return render(req,'landing.html')