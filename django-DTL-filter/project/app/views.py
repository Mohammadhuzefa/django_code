from django.shortcuts import render

# Create your views here.


def lending(r):
    d={
        'name':'jatin',
        'class':'bca',
        'city':'bhopal',
        'p':'hello django',
        'p2':'this is cybrom',
        'l':['python',10,20,30]
    }
    # return render(r,'landing.html',d)
    return render(r,'lending.html',{'data':d})

def my_for(req):
    d=[{'n':'Neeraj',
        'c':'Bhopal',
        'r':'Faculty'},
       {'n':'Sumit',
        'c':'Bari',
        'r':'Student'},
       {'n':'Arshan',
        'c':'Bhopal',
        'r':'Student'}]
    return render(req,'my_for.html',{'data':d})

def base(req):
   
    # return render(r,'landing.html',d)
    return render(req,'base.html')

def home(req):
   
    return render(req,'home.html')

def index(req):
   
    return render(req,'index.html')

# def data(req):
#    print("hello")
