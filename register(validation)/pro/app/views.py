# from django.shortcuts import render , redirect
# from .models import Student

# # Create your views here.

# def landing(req):
#     return render(req,'landing.html')

# def Register(req):
#     if req.method=='POST':
#         n = req.POST.get('name')
#         e = req.POST.get('email')
#         c = req.POST.get('contact')
#         p = req.POST.get('password')

#         user = Student.objects.filter(email=e)

#         if user:
#             req.session['x']="Email already exist"
#             return redirect('Register')
#         else:
#             Student.objects.create(name=n,email=e,contact=c,password=p)
#             return redirect('Login')
        
#     x = req.session.get('x','') 
    
#     return render(req,'Register.html',{'x':x})


# def Login(req):
#     if req.method == 'POST':
#         e = req.POST.get('email')
#         p = req.POST.get('password')
#         print(e, p)
#         user = Student.objects.filter(email=e)
#         print(user.password)
#         if user:

#             userdata = Student.objects.get(email=e)
#             if p==userdata.password:
                
#                 id = userdata.id
#                 req.session['user_id']=id
#                 return redirect('dashboard')
#             else:
#                 req.session['y']="Email and password not match"
#                 return redirect('Login')
            
#         else:
                       
#             req.session['x']="Email Not Register"
#             return redirect('Register')
#     y = req.session.get('y','')    
#     return render(req,'Login.html',{'y':y})


# def dashboard(req):
#     if 'user_id' in req.session:
#         id = req.session['user_id']
#         userdata = Student.objects.get(id=id)
#         data = {
#             'name':userdata.name,
#             'email':userdata.email,
#             'contact':userdata.contact,
#             'password':userdata.password,
#         }
#         return render(req,'dashboard.html',{'data':data})
#     else:
#         return redirect('Login')


# def logout(req):
#     if 'user_id' in req.session:
#         req.session.flush()
#         return redirect('Login')
#     else:
#         return redirect('Login')



from django.shortcuts import render,redirect
from .models import Student


def landing(req):
    return render(req,'landing.html')

def home(req):
    return render(req,'home.html')

def about(req):
    return render(req,'about.html')

def contact(req):
    return render(req,'contact.html')

def services(req):
    return render(req,'services.html')

# Create your views here.
def Register(req):
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
            return redirect('Register')
        else:
            Student.objects.create(name=n,email=e,contact=c,password=p)
            return redirect('Login')
    else:
        if 'x' in req.session:
            x = req.session['x']
            req.session.flush()
            return render(req,'Register.html',{'x':x})
        elif 'y' in req.session:
            x = req.session['y']
            req.session.flush()
            return render(req,'Register.html',{'x':x})
        else:
            return render(req,'Register.html')

def Login(req):
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
                return redirect('Login')
            
        else:
                       
            req.session['y']="Email Not Register"
            return redirect('register')
    else:
        if 'y' in req.session:
            y = req.session['y']
            return render(req,'Login.html',{'y':y})
        else:
            return render(req,'Login.html')

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
        return redirect('Login')
        

def Logout(req):
    if 'user_id' in req.session:
        req.session.flush()
        return redirect('Login')
    else:
        return redirect('Login')