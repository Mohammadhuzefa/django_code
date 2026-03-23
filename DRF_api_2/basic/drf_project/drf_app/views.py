from django.shortcuts import render
from .models import data
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def detail(req,pk):
    user = data.objects.filter(id=pk)
    if user:
        if req.method=='PUT':
            json=req.body
            print(json)
            print(type(json))
            stream = io.BytesIO(json)
            print(stream)
            print(type(stream))
            p_n_data = JSONParser().parse(stream)
            p_o_data = data.objects.get(id=pk) #------------------------------
            print(p_n_data)
            print(type(p_n_data))
            serializer = StudentSerializers(p_o_data,data=p_n_data) #     added p_o_data--------
            if serializer.is_valid():
                print(serializer.validated_data)
                serializer.save()
                dat={'msg':'data updated succesfully ! '}
                json = JSONRenderer().render(dat)
                return HttpResponse(json,content_type="application/json")
            else:
                dat=serializer.errors
                json = JSONRenderer().render(dat)
                return HttpResponse(json,content_type="application/json")
            
        elif req.method=='PATCH':
            json=req.body
            print(json)
            print(type(json))
            stream = io.BytesIO(json)
            print(stream)
            print(type(stream))
            p_n_data = JSONParser().parse(stream)
            p_o_data = data.objects.get(id=pk)
            print(p_n_data)
            print(type(p_n_data))
            serializer = StudentSerializers(p_o_data,data=p_n_data,partial=True) # added only partial=True--------
            if serializer.is_valid():
                print(serializer.validated_data)
                serializer.save()
                dat={'msg':'data partially updated succesfully ! '}
                json = JSONRenderer().render(dat)
                return HttpResponse(json,content_type="application/json")
            else:
                dat=serializer.errors
                json = JSONRenderer().render(dat)
                return HttpResponse(json,content_type="application/json")
            
        elif req.method=='DELETE':
            xyz = data.objects.get(id=pk)
            xyz.delete()
            dat={'msg':'data deleted succesfully ! '}
            json = JSONRenderer().render(dat)
            return HttpResponse(json,content_type="application/json")

        x=data.objects.get(id=pk)
        ser=StudentSerializers(x)
        print(ser)
        print(ser.data)
        json = JSONRenderer().render(ser.data)
        print(json)
        return HttpResponse(json,content_type="application/json")
    else:
        dat={'msg':'Id not found our database '}
        json = JSONRenderer().render(dat)
        return HttpResponse(json,content_type="application/json")



@csrf_exempt
def listt(req):
    if req.method=='POST':
        json=req.body
        print(json)
        print(type(json))
        stream = io.BytesIO(json)
        print(stream)
        print(type(stream))
        p_data = JSONParser().parse(stream)
        print(p_data)
        print(type(p_data))
        serializer = StudentSerializers(data=p_data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            dat={'msg':'data created succesfully ! '}
            json = JSONRenderer().render(dat)
            return HttpResponse(json,content_type="application/json")
        else:
            dat=serializer.errors
            json = JSONRenderer().render(dat)
            return HttpResponse(json,content_type="application/json")
    x=data.objects.all()
    ser=StudentSerializers(x,many=True)
    print(ser)
    print(ser.data)
    json = JSONRenderer().render(ser.data)
    print(json)
    return HttpResponse(json,content_type="application/json")





