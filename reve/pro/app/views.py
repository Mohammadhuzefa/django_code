from django.shortcuts import render,redirect

from .models import Student
# Create your views here.
def register(req):
    if req.method=="POST":
        # print(req.POST)
        n = req.POST.get('name')
        e = req.POST.get('email')
        c = req.POST.get('contact')
        p = req.POST.get('password')
        user = Student.objects.filter(email=e)
        if user:
            # return render(req,'register.html',{"msg":"Email already exist"})
            req.session['x']="Email already exist"
            return redirect('register')
        else:
            Student.objects.create(name=n,email=e,contact=c,password=p)
            return redirect('login')
    else:
        if 'x' in req.session:
            x = req.session['x']
            req.session.flush()
            return render(req,'register.html',{'x':x})
        elif 'y' in req.session:
            x = req.session['y']
            req.session.flush()
            return render(req,'register.html',{'x':x})
        else:
            return render(req,'register.html')

def login(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')
        print(e, p)
        user = Student.objects.filter(email=e)
        if user:
            userdata = Student.objects.get(email=e)
            if p==userdata.password:
                id = userdata.id
                req.session['user_id']=id
                return redirect('dashboard')
            else:
                req.session['y']="Email and password not match"
                return redirect('login')
        else:         
            req.session['y']="Email Not Register"
            return redirect('register')
    else:
        if 'y' in req.session:
            y = req.session['y']
            return render(req,'login.html',{'y':y})
        else:
            return render(req,'login.html')

def dashboard(req):
    if 'user_id' in req.session:
        id = req.session['user_id']
        userdata = Student.objects.get(id=id)
        data = {
            'name':userdata.name,
            'email':userdata.email,
            'contact':userdata.contact,
            'password':userdata.password,
        }
        return render(req,'dashboard.html',{'data':data})
    else:
        return redirect('login')
        

def logout(req):
    if 'user_id' in req.session:
        req.session.flush()
        return redirect('login')
    else:
        return redirect('login')
    

def home(req):
    
     if 'user_id' in req.session:
        id = req.session['user_id']
        userdata = Student.objects.get(id=id)
        data = {
            'name':userdata.name,
            'email':userdata.email,
            'contact':userdata.contact,
            'password':userdata.password,
        }
        return render(req,'home.html',{'data':data})
     return render(req,'home.html')

def about(req):
     if 'user_id' in req.session:
        id = req.session['user_id']
        userdata = Student.objects.get(id=id)
        data = {
            'name':userdata.name,
            'email':userdata.email,
            'contact':userdata.contact,
            'password':userdata.password,
        }
        return render(req,'about.html',{'data':data})
     return render(req, 'about.html')
