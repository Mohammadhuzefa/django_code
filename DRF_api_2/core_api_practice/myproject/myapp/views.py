from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from  myapp.models import Stu
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Create your views here.s
import json
# gett
# def listt(req):
#     stu_data=Stu.objects.all()
#     p_data=list(stu_data.values())
#     j_data=json.dumps(p_data)
#     print(j_data)
#     return HttpResponse(j_data,content_type='application/json')
#     # return JsonResponse(j_data,safe=False)

# postt
@csrf_exempt
def listt(req):
    if req.method=='POST':
        data=req.body
        p_data=json.loads(data)
        n,e,c,a=p_data.get('name'),p_data.get('email'),p_data.get('city'),p_data.get('age')
        Stu.objects.create(name=n,email=e,city=c,age=a)
        d={'msg':'ban gya data'}
        j_data=json.dumps(d)
        return JsonResponse(d,safe=False)
    else:
        data=Stu.objects.all()
        p_data=list(data.values())
        j_data=json.dumps(p_data)
        return JsonResponse(p_data,safe=False)
    
# @csrf_exempt
# def listt(req):
#     if req.method != 'POST':
#         return JsonResponse({'error': 'Invalid request'}, status=405)

#     data = json.loads(req.body)
#     Stu.objects.create(
#         name=data.get('name'),
#         email=data.get('email'),
#         city=data.get('city'),
#         age=data.get('age')
#     )

#     return JsonResponse({'msg': 'ban gya data'})


# gwet thorugh id
# def detail(req,pk):
#     stu_data=Stu.objects.get(id=pk)
#     p_data=model_to_dict(stu_data)
#     j_data=json.dumps(p_data)
#     # return JsonResponse(j_data,safe=False)
#     return HttpResponse(j_data,content_type='application/json')

# put
@csrf_exempt
def detail(req,pk):
    user=Stu.objects.filter(id=pk)
    if user:
        if req.method=='PUT':
             data=req.body
             p_data=json.loads(data)
             if 'name' in p_data and 'email' in p_data and 'city' in p_data and 'age' in p_data:
                n,e,c,a=p_data.get('name'),p_data.get('email'),p_data.get('city'),p_data.get('age')
                old_data=Stu.objects.get(id=pk)
                old_data.name=n
                old_data.email=e
                old_data.city=c
                old_data.age=a
                old_data.save()
                d={'msg':'ho gya update'}
                j_data=json.dumps(d)
                return JsonResponse(d,safe=False)
             else:
                 d={'msg':"puri to dded be"}
                 return JsonResponse(d,safe=False)
        if req.method=='PATCH':
            data=req.body
            p_data=json.loads(data)
            n,e,c,a=p_data.get('name'),p_data.get('email'),p_data.get('city'),p_data.get('age')
            old_data=Stu.objects.get(id=pk)
            if 'name' in p_data:
                old_data.name=n
            if 'email' in p_data:
                old_data.email=e
            if 'city' in p_data:
                old_data.city=c
            if 'age' in p_data:
                old_data.age=a
            old_data.save()
            d={'msg':'object partially upadted'}
            return JsonResponse(d,safe=False)
       
        if req.method=='DELETE':
            use=Stu.objects.get(id=pk)
            use.delete()
            d={'msg':'gya tata by by !'}
            return JsonResponse(d,safe=False)

        
    else:
        d={'msg':'user nhi he be '}
        return JsonResponse(d,safe=False)       

        

                

@csrf_exempt   
def data(req):
    j_data = req.body 
    p_data = json.loads(j_data)
    print(p_data)
    print('id' in p_data)

    if 'id' in p_data:
        oid = p_data.get('id')
        obj_data = Stu.objects.filter(id=oid) 
        if obj_data:
            if req.method=='PUT':
                pk=p_data.get('id')
                n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('city'),p_data.get('age')
                # if n and e and c and a:
                if 'name' in p_data and 'email' in p_data and 'city' in p_data and 'age' in p_data:
                    old_obj = Stu.objects.get(id=pk)
                    old_obj.name = n
                    old_obj.email = e 
                    old_obj.city = c
                    old_obj.age = a
                    old_obj.save()
                    d={'msg':'Object updated successfully.........'}
                    j_data = json.dumps(d)
                    return HttpResponse(j_data,content_type='application/json')
                else:
                    d={'msg':'Some required filelds are missing'}
                    j_data = json.dumps(d)
                    return HttpResponse(j_data,content_type='application/json')

            elif req.method=='PATCH':
                if p_data:
                    pk=p_data.get('id')
                    # p_data = json.loads(data)
                    n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('city'),p_data.get('age')
                    old_obj = Stu.objects.get(id=pk)
                    if 'name' in p_data:
                        old_obj.name = n
                    if 'email' in p_data:
                        old_obj.email = e
                    if 'city' in p_data:
                        old_obj.city = c
                    if 'age' in p_data:
                        old_obj.age = a
                    old_obj.save()
                    d={'msg':'Object partially updated successfully.........'}
                    j_data = json.dumps(d)
                    return HttpResponse(j_data,content_type='application/json')
                else:
                    d={'msg':'We need atleast one field to update but we don"t provide '}
                    j_data = json.dumps(d)
                    return HttpResponse(j_data,content_type='application/json')

            elif req.method=='DELETE':
                pk=p_data.get('id')
                old_obj = Stu.objects.get(id=pk)
                old_obj.delete()
                d={'msg':'Object deleted successfully........!'}
                j_data = json.dumps(d)
                return HttpResponse(j_data,content_type='application/json')
            
            pk=p_data.get('id')
            emp_data = Stu.objects.get(id=pk)
            p_data = model_to_dict(emp_data)
            j_data = json.dumps(p_data)
            return HttpResponse(j_data,content_type='application/json')
        else:
            d={'msg':'Object not present in our database..........'}
            j_data = json.dumps(d)
            return HttpResponse(j_data,content_type='application/json')
            
    else:
        if req.method=='POST':
            if 'name' in p_data and 'email' in p_data and 'age' in p_data and 'city' in p_data: 
                n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('city'),p_data.get('age')
                Stu.objects.create(name=n,email=e,city=c,age=a)
                d={'msg':'object created successfully.......','data':p_data}
                j_data = json.dumps(d)
                return HttpResponse(j_data,content_type='application/json')  
            else:
                d={'msg':'Some required fields are missing............'}
                j_data = json.dumps(d)
                return HttpResponse(j_data,content_type='application/json') 
        emp_data = Stu.objects.all()
        p_data = list(emp_data.values())
        j_data = json.dumps(p_data)
        return HttpResponse(j_data,content_type='application/json') 
        

    


