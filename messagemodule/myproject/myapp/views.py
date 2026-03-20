from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.

def index(req):
    messages.info(req,"welcome to my page")
    messages.error(req,"error find")
    messages.success(req,"success")
    messages.debug(req,"debug")
    messages.warning(req,"warning")
    return redirect(home)
    # return render(req,'home.html')



def home(req):
    return render(req,'home.html')
