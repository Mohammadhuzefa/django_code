from django.shortcuts import render
from .forms import Studentform
# Create your views here.
def landing(req):
    return render(req,'landing.html')

def register(req):
    xyz=Studentform()
    return render(req,'register.html',{'fm':xyz})