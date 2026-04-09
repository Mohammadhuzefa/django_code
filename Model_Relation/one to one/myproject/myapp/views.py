from django.shortcuts import render
from myapp.models import Stu,Adhaar
# Create your views here.
def landing(req):
    return render(req,'landing.html')


def forward_access(req):
    # data=Stu.objects.all()
    # print(data.query)
    data=Stu.objects.select_related("a_no")
    print(data.query)
    return render(req,'forward_access.html',{'data':data})

def reverse_access(req):
    data1=Adhaar.objects.all()
    print(data1.query)
    data2=Adhaar.objects.select_related("stu")
    print(data2.query)
    return render(req,'reverse_access.html',{'data':data1})