from django.shortcuts import render,redirect
from myapp.models import emp
# Create your views here.

def login(req):
      if 'admin_e' in req.session and 'admin_p' in req.session:
          
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'fname': req.session['admin_n']
        }
          return render(req,'admindpanel.html', {'data': a_data})
      else:
             if 'emp_id' in req.session:
                emp_id=req.session.get('emp_id')
                emp_data=emp.objects.get(id=emp_id)
                data={
                'fname':emp_data.fname,
                'email':emp_data.email,
                'DOB':emp_data.DOB,
                'gender':emp_data.gender,
                'mobile':emp_data.mobile,
                }
                return render(req,'emppanel.html',{'data':data})
      if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')
        if e == 'admin@gmail.com' and p == 'admin':
                req.session['admin_e'] = e
                req.session['admin_p'] = p
                req.session['admin_n'] = 'admin'
                return redirect('admindpanel')
        else:
            user = emp.objects.filter(email=e)
            if user:
                user=emp.objects.get(email=e)         
                if e==user.email and p==user.mobile:
                    # req.session['emp_e'] = e
                    # req.session['emp_p'] = p
                    # req.session['emp_n'] = 'emp'
                    req.session['emp_id']=user.id
                    return redirect('emppanel')
                else:
                    x={'g':"wrong passord or username"}
                    return render(req,'login.html',{'data':x})
            else:
                x={'g':"Invalid Email"}
                return render(req,'login.html',{'data':x})
      return render(req, 'login.html')

