from django.shortcuts import render , redirect
from .models import Employee


# Create your views here.


def landing(req):
    return render(req,'landing.html')

def login(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')
        print(e,p)

        if e == 'admin@gmail.com' and p == 'admin':
            req.session['admin_e'] = e 
            req.session['admin_p'] = p
            req.session['admin_n'] = 'admin'
            return redirect('adminDash')
        
        user = Employee.objects.filter(email=e)
        if user:
            userdata = Employee.objects.get(email=e)
            if p==userdata.id:
                id = userdata.id
                req.session['user_id']=id
                return redirect('adminDash')
            
            else:
                req.session['y'] = "Email and Password not match"
                return redirect('login')
            

        else:
            req.session['x']="Email not register"
            return redirect('register')
        
    y = req.session.get('y','')
    return render(req,'login.html',{'y':y})
        
        
        



def register(req):
    return render(req,'register.html')

def adminDash(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
        a_email = req.session['admin_e']
        p_admin = req.session['admin_p']
        n_admin = req.session['admin_n']
        a_data = {
            'email' : e_email,
            'password':p_admin,
            'name':n_admin

        }
        return render(req,'adminDash.html',{'data':a_data})
    else:
        return redirect('login')




