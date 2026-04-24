from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import json
from django.urls import reverse
from urllib.parse import urlencode 

# Create your views here.
 
def  home(r):
    return HttpResponse("hello user")
 
    
def  home2(r):
    return HttpResponse("<h1 style='color : blue;'>hello user</h1>")
 
    

def  home3(r):
    return HttpResponse("hello user how are you",content_type="text/plain")
 
def  home4(r):
    html="<h1>hello puju</h1>"
    return HttpResponse(html,content_type="text/html")
 

def  home5(r):
    jsn={"name":"puju","age":55}
    y=json.dumps(jsn)
    return HttpResponse(y,content_type="application/json")
 


def  home6(r):
    return render(r,"my_render.html")
 
# def  home8(r):
#     d={
#         "name":"jatin"
#     }
#     return render(r,"my_render.html",d)
 

def  home8(r,x):
    d={
        'x':x
    }
    return render(r,"my_render.html",d)


def  home9(r,x):
    d={
        'str':x
    }
    return render(r,"my_render.html",d)

def  home10(r,name,clas):
    d={
        'name':name,
        'clas':clas

    }
    return render(r,"my_render.html",d)


def  homejson(r):
    d=("pooja rani")
    return JsonResponse(d,safe=False)


def  re(r):
    return redirect("home4")


def my_redirect1(req):
    url = reverse('my_redirect2')
    data = urlencode({'name': 'sumit', 'age': 19})
    return redirect(f'{url}?{data}')    


# def my_redirect2(req):
#     print("hello")
#     return HttpResponse(req.GET)    

def my_redirect2(req):
    name = req.GET.get('name')
    age = req.GET.get('age')
    print(req.GET)
    return HttpResponse(f"Name: {name}, Age: {age}",content_type='text/plain')

# def my_redirect2(req):
#     return HttpResponse(str(dict(req.GET)))
