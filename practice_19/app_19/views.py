from django.shortcuts import render
from .forms import StudentForm,StudentLoginForm
from django.shortcuts import render, redirect
from .models import  Emp,Task
from django.core.mail import send_mail
from django.views.decorators.cache import never_cache
import random
def login(request):
    if request.method == "POST":
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = Emp.objects.filter(email=email).first()

            if user:
                if user.phone == password:
                    request.session['id']=user.id
                    return redirect("home")
                
                else:
                    form.add_error(None, "Invalid Password")
            else:
                form.add_error(None, "Email not registered")

    else:
        form = StudentLoginForm()

    return render(request, "Login.html", {"form": form})

# Create your views here.
@never_cache
 
def home(req):
    if 'id' in req.session:
        uid=req.session.get('id')
        userid=Emp.objects.get(id=uid) 
        return render(req,'Home.html',{'data':userid})
    else:
        return redirect('login')

def Sign(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")  # ✅ Only redirect if form is valid
        # If form is invalid, it will fall through and render the template with errors
    else:
        form = StudentForm()
    return render(request, "Sign.html", {"form": form})


@never_cache
def logout(req):
    if 'id' in req.session:
        req.session.flush()
        return redirect('login')
    else:
        return redirect('login')


def forget_password(req):
    return render(req,"forget_password.html")
   
def forget(req):
    otp=req.session.get('otp')
    if not otp:
        if req.method=='POST':
            email=req.POST.get('email')
            uemail=Emp.objects.filter(email=email)
            if uemail:
                user=Emp.objects.get(email=email)
                otp=random.randint(1111,9999)
                req.session['email']=user.email
                req.session['otp']=otp
                send_mail(
                      subject="Forget password",
                      message=f'User Email OTP: {otp}',
                      from_email="jattfact@gmail.com",  
                      recipient_list=[user.email],
                      fail_silently=False,
                   )
                return render(req,'otp.html')
            else:
                return redirect('forget_password')
            
    else:
        return render(req,'otp.html')
            
            
def otp(req):
    pass

def newpassword(req):
    if req.method=='POST':
        oyp=req.POST.get('otp')
        sotp=req.session.get('otp')
        if str(oyp)==str(sotp):
            email=req.session.get('email')
            req.session.pop('otp')
            return render(req,'set.html',{'email':email})
        else:
            return render(req,'otp.html')

def set(req):
    pass


def newpass(req):
    if req.method=='POST':
        new_password=req.POST.get('new_password')
        confirm_password=req.POST.get('confirm_password')
        if new_password==confirm_password:
            uemial=Emp.objects.get(email=req.session.get('email'))
            uemial.phone=new_password
            uemial.save()
            return redirect('login')
    


def addtask(req):
    if 'id' in req.session:
        uid=req.session.get('id')
        userid=Emp.objects.get(id=uid) 
        task=req.POST.get('task')
        Task.objects.create(task=task)
        data1=Task.objects.all()

        return render(req,'home.html',{'data1':data1,'data':userid})

def edit(req,pk):
      if 'id' in req.session:
        uid=req.session.get('id')
        userid=Emp.objects.get(id=uid) 
        data1=Task.objects.get(id=pk)
        return render(req,'edit.html',{'data1':data1,'data':userid})

def deli(req,pk):
    t=Task.objects.get(id=pk)
    t.delete()
    data1=Task.objects.all()
    return render(req,'home.html',{'data1':data1})


# def edi(req,pk):
#     if req.method=='POST':
#         t=req.POST.get('taskk')
#         data1=Task.objects.get(id=pk)
#         data1.task=t
#         data1.save()
#         return render(req,'home.html')
  
#     return render(req,'home.html')
    
        
def edi(req,pk):
    if req.method == "POST":
        t = req.POST.get('taskk')

        task = Task.objects.get(id=pk)
        task.task = t
        task.save()

        return redirect('home')   # 🔥 redirect use karo

    return redirect('home')