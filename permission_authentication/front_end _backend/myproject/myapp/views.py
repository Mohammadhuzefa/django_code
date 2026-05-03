from django.shortcuts import render

# Create your views here.
 

from .models import Officer
from django.shortcuts import get_object_or_404
from .serializers import OfficerSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

class OfficerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Officer.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication] objectt lvel 
    serializer_class = OfficerSerializer

def gen_jwt(req):
    return render(req,'jwt.html')

def genrate_jwt(req):
    from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Officer

def gen_jwt(request):
    return render(request,'gen_jwt.html')


def genrate_jwt(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        post = request.POST.get('post')
        salary = request.POST.get('salary')
        roll = request.POST.get('roll')
        password = request.POST.get('password')

        # officer create
        # officer = Officer.objects.create(
        #     name=name,
        #     email=email,
        #     post=post,
        #     salary=salary,
        #     roll=roll,
        #     password=password
        # )

        # JWT generate
        # refresh = RefreshToken()
        # refresh['email'] = officer.email
        # refresh['name'] = officer.name
        # refresh['role'] = officer.roll

        # token = str(refresh.access_token)

        # return render(request,'jwt.html',{'token':token})

    return render(request,'gen_jwt.html')