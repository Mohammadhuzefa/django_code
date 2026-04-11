from django.shortcuts import render
from my_app.models import Stu
# Create your views here.
def home(req):
    # s=Stu.objects.last()
    s=Stu.objects.all()
    return render(req,'home.html',{'s':s})