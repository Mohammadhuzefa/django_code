from django.shortcuts import render

# Create your views here.


def landing(req):
    return render(req,'landing.html')




def deli(req):
    return render(req,'deli.html')


def night(req):
    return render(req,'night.html')



  
def sign(req):
    return render(req,'sign.html')
    
  
def login(req):
    return render(req,'login.html')    