from django.shortcuts import render,redirect
from app.models import dep,emp

# Create your views here.
# def landing(req):
#         if 'admin_e' in req.session and 'admin_p' in req.session:
#           a_data = {
#             'email': req.session['admin_e'],
#             'password': req.session['admin_p'],
#             'name': req.session['admin_n']
#         }
#           return render(req,'landing.html', {'data': a_data})
#         else:
#              return render(req,'landing.html')

def base(req):
    return render(req,'base.html')

# def lo(req):
#     if req.method == 'POST':
#         e = req.POST.get('email')
#         p = req.POST.get('password')
#         if e == 'admin@gmail.com' and p == 'admin':
#             req.session['admin_e'] = e
#             req.session['admin_p'] = p
#             req.session['admin_n'] = 'admin'
#             return redirect('admindashboard')
#         else:
#             x={'g':"wrong passord or username"}
#             return render(req,'lo.html',{'data':x})

#     return render(req, 'lo.html')

def admindashboard(req):
    # Admin Session Check
    if 'admin_e' in req.session and 'admin_p' in req.session:
        a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
        return render(req, 'admindashboard.html', {'data': a_data})
    else:
        return redirect('lo')
    


def logout(req):
    if 'admin_e' in req.session:
        req.session.flush()
        return redirect('landing')
    else:
        return redirect('lo')
   

# def tr(req):
#        if 'admin_e' in req.session and 'admin_p' in req.session:
#         a_data = {
#             'email': req.session['admin_e'],
#             'password': req.session['admin_p'],
#             'name': req.session['admin_n']
#         }
#         return render(req,'tr.html', {'data': a_data})
#        else:
#             return render(req,'tr.html')

# def o(req):
#         if 'admin_e' in req.session and 'admin_p' in req.session:
#          a_data = {
#             'email': req.session['admin_e'],
#             'password': req.session['admin_p'],
#             'name': req.session['admin_n']
#         }
#          return render(req,'o.html', {'data': a_data})
#         else:
#             return render(req,'o.html')



# def sin(req):
#           if 'admin_e' in req.session and 'admin_p' in req.session:
#            a_data = {
#             'email': req.session['admin_e'],
#             'password': req.session['admin_p'],
#             'name': req.session['admin_n']
#         }
#            return render(req,'sin.html', {'data': a_data})
#           else:
#                return render(req,'sin.html')
 

# def free(req):
#             if 'admin_e' in req.session and 'admin_p' in req.session:
#              a_data = {
#             'email': req.session['admin_e'],
#             'password': req.session['admin_p'],
#             'name': req.session['admin_n']
#         } 
#              return render(req,'free.html', {'data': a_data})
#             else:
#                  return render(req,'free.html')

# def x(req):
#          if 'admin_e' in req.session and 'admin_p' in req.session:
#           a_data = {
#             'email': req.session['admin_e'],
#             'password': req.session['admin_p'],
#             'name': req.session['admin_n']
#         }
#           return render(req,'x.html', {'data': a_data})
#          else:
#               return render(req,'x.html')


def save_department(req):
    if req.method=='POST':
          dname=req.POST.get('dept_name')
          dcode=req.POST.get('dept_code')
          dhead=req.POST.get('dept_head')
          dbudget=req.POST.get('dept_budget')
          ddesc=req.POST.get('dept_desc')
          deptdata=dep.objects.filter(dept_name=dname)
          if not deptdata:
            dep.objects.create(dept_name=dname,dept_code=dcode,dept_head=dhead,dept_budget=dbudget,dept_desc=ddesc)
            return redirect("add_department")
          else:
            return redirect('add_department')
     
    return redirect('lo')

    
def add_department(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          return render(req,'admindashboard.html', {'data': a_data,"add_department":True})
    else:
        msg={'msg':'login first'}
        return render(req,"lo.html",{'msg':msg})

def addemp(req):
      if req.method=='POST':
           fname=req.POST.get('fname')
           lname=req.POST.get('lname')
           email=req.POST.get('email')
           img=req.FILES.get('img')
           adhaar=req.FILES.get('adhaar')
           code=req.POST.get('code')
           mobile=req.POST.get('mobile')
           DOB=req.POST.get('DOB')
           gender=req.POST.get('gender')
           edu=req.POST.getlist('edu')
           dept=req.POST.get('dept')
           emp.objects.create(fname=fname,lname=lname,email=email,img=img,adhaar=adhaar,code=code,mobile=mobile,DOB=DOB,gender=gender,edu=edu,dept=dept)
           return render(req,'admindashboard.html')
      else:
           return render(req,'admindashboard.html')