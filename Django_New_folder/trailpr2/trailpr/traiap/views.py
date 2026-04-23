from django.shortcuts import render,redirect
from traiap.models import  Student
# Create your views here.




def hero(req):
    return render(req,'hero.html')

def second(req):
    return render(req,'second.html')
def career(req):
    return render(req,'career.html')
# def log(req):
#     return render(req,'log.html')
# def sign(req):
#     return render(req,'sign.html')



def sign(req):
    if req.method=="POST":
        print(req.POST)
        n = req.POST.get('name')
        e = req.POST.get('email')
        p = req.POST.get('password')
        user = Student.objects.filter(email=e)
        if user:
            # return render(req,'register.html',{"msg":"Email already exist"})
            req.session['x']="Email already exist"
            return redirect('sign')
        else:
            Student.objects.create(name=n,email=e,pas=p)
            return redirect('log')
    x = req.session.get('x')     
    return render(req,'sign.html',{'x':x})
 
def log(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')
        print(e, p)

        Student.objects.create(Email=e, Pas=p)

        return render(req, 'login.html', {'msg': 'Registered successfully'})

    return render(req, 'login.html')