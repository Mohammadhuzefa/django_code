from django.shortcuts import render
from .models import car,fuel
# Create your views here.
def landing(req):
    # froward aces
    cal=car.objects.all()
    mobil=fuel.objects.all()
    return render(req,'landing.html',{'mobil':mobil,'cal':cal})
