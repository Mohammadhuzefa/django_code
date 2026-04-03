from django.shortcuts import render
from .models import Patient

# Create your views here.


from django.shortcuts import render
from .models import Patient


from django.shortcuts import render
from .models import Patient


def landing(req):

    if req.method == "POST":
        n = req.POST.get('name')
        a = req.POST.get('age')
        g = req.POST.get('gender')
        m = req.POST.get('mobile')
        e = req.POST.get('email')
        d = req.POST.get('department')
        da = req.POST.get('date')

        data=Patient.objects.create(
            n=n,
            a=a,
            g=g,
            m=m,
            e=e,
            d=d,
            da=da
        )

        return render(req,'landing.html',{'data':data})   # best practice

    return render(req, 'landing.html')

def doctor(req):
    data=Patient.objects.all()
    return render(req,'doctor.html',{'data':data})