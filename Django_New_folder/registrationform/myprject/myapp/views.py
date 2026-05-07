from django.shortcuts import render
from .models import Student
# Create your views here.


def form(r):
    return render(r,'form.html')

def data(r):

 if r.method=='POST':
    # print(r.GET) #all
    # print(r.POST) #all
    # print(r.FILES) #binary content
    # print(r.method) #method
    n=r.POST.get('name')
    e=r.POST.get('email')
    tel1=r.POST.get('tel1')
    tel2=r.POST.get('tel2')
    q = r.POST.getlist('qualifiaction')
    city=r.POST.get('city')
    g=r.POST.get('gender')
    print(n,e,tel1,tel2,q,city,g,sep=',')
    pic=r.FILES.get('image')
    d=r.FILES.get('Document')
    print(pic)
    print(type(n),type(e),type(tel1),type(tel2),type(q),type(city),type(g),type(pic),sep=" ")
    Student.objects.create(name=n,email=e,contact=tel1,tel=tel2,quali=q,state=city,gender=g,img=pic,Document=d)

    # files ke files 
    # get me get wali
# muti valuedict me file 
# queery me a sab
# django me small post and capital dno
# form se post and req me POST
# csrf farzi se bacahta he
# input se sab string me 
#get ki vajah se url me dstat aa rha he and post me
# json jaise me print kaise


# models me class me table col and row
# and charfiles(max50)dena imp and max(255) aur file sis binary content so we  not stored in data bases and stroe url then where will file go 
# and str ko int me convert krna pdega aa
    # ge 

    # pilloow inmg ke liye he

    # make migration se wurru aye gi intial ooo0 mpe orm querry
#  python manage.py makemigrations  models ko orm me convert krta he 
# python me manage.py migrate tablebneyag
# promary not null unswue