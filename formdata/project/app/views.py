from django.shortcuts import render
from .models import Student

# Create your views here.
def index(req):
   
    return render(req,'index.html')


def formdata(req):
    print(req.method)
    print(req.GET)
    print(req.POST)
    print(req.FILES)
    n=req.POST.get('name')
    e=req.POST.get('email')
    c=req.POST.get('contact')
    ed=req.POST.get('education')
    s=req.POST.get('city')
    g=req.POST.get('gender')
    i=req.FILES.get('image')
    d=req.FILES.get('document')
    a=req.FILES.get('audio')
    v=req.FILES.get('video')

    # print(n,e,tel1,tel2,q,s,g,sep=',')

    Student.objects.create(Name=n,Email=e,Contact=c,Education=ed,City=s,Gender=g,Image=i,Document=d,Audio=a,Video=v)
