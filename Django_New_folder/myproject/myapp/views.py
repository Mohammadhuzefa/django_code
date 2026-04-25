from django.shortcuts import render

# Create your views here.

def landin(r):
 return render(r,'landin.html')


def data(r):
 print("hello")
 print(r.POST)
 print(r.FILES)
 