from django.shortcuts import render
from .models import Student, Aadhar

# Create your views here.
def landing(req):
    return render (req,"landing.html")

def forward_access():
    stu_data=Student.object()
    print(stu_data.query)
    for i in stu_data:
        print(i.name,i.email,i.contact),
        i.city,i.a_no.aadhar_no,
        i.a_no.created_data,
        i.a_no.created_by

def reverse_access(req):
    a_data=Aadhar.object.all()
    for i in a_data:
        print(i.aadhar_no,i.create_data,i.create_by)
        print(i.student.name,i.student.email,i.student.contact,i.student.city)