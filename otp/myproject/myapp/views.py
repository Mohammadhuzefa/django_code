from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def resetp(req):
    return render(req,'resetp.html')