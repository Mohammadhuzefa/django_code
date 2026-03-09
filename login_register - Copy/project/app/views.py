from django.shortcuts import render , redirect
from app.models import Student

# Create your views here.

def base(req):
    return render(req,'base.html')

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
    x = req.session.get('x','') 
    
    return render(req,'register.html',{'x':x})

def login(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')
        print(e, p)
        if e == 'admin@gmail.com' and p == 'admin':
            req.session['admin_e']=e
            req.session['admin_p']=p
            req.session['admin_n']='admin'
            return redirect('dashboard')
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
                       
            req.session['x']="Email Not Register"
            return redirect('register')
    y = req.session.get('y','')    
    return render(req,'login.html',{'y':y})

def dashboard(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
        a_email = req.session['admin_e']
        p_admin = req.session['admin_p']
        n_admin = req.session['admin_n']
        a_data = {
            'email':a_email,
            'password':p_admin,
            'name':n_admin
        }
        return render(req,'admindashboard.html',{'data':a_data})
    elif 'user_id' in req.session:
        id = req.session['user_id']
        userdata = Student.objects.get(id=id)
        data = {
            'name':userdata.name,
            'email':userdata.email,
            'contact':userdata.contact,
            'password':userdata.password
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
    
