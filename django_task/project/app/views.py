from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def home(req):
    return render(req,'home.html')

def base(req):
    return render(req,'base.html')
