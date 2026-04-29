from django.shortcuts import render

# Create your views here.
def landing(r):
    return render(r,'landing.html')


def pro(r):
    return render(r,'pro.html')

def cor(r):
    return render(r,'cor.html')


def gif(r):
    return render(r,'gif.html')