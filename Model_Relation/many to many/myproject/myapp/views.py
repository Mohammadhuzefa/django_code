from django.shortcuts import render
from myapp.models import Course,Student
# Create your views here.
def fore(req):
    # data=Student.objects.all()
    data=Student.objects.prefetch_related('courses')
    return render(req,'fore.html',{'data':data})

def rev(req):
    # data=Course.objects.all()
    data=Course.objects.prefetch_related('puju')
    return render(req,'rev.html',{'data':data})

def landing(req):
    return render(req,'landing.html')