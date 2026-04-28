from django.shortcuts import render
from .forms import Studentform
 # Create your views here.
def Form(req):
    data=Studentform()
    return render(req,'Form.html',{'data':data})


from django.shortcuts import render, redirect
from .forms import Studentform

def Form(req):
    if req.method == 'POST':
        form = Studentform(req.POST)
        
        if form.is_valid():
            print(form.cleaned_data)   # is_valid ke baad hi use karo
            form.save()
            return redirect('Form')
    else:
        form = Studentform()   # GET request ke liye empty form

    return render(req, 'Form.html', {'data': form})
 