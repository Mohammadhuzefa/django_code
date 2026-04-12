# # from django.shortcuts import render
# # from .models import Stu
# # from django.http import JsonResponse,HttpResponse
# # import json
# # from django.views.decorators.csrf import csrf_exempt
# # from django.forms.models import model_to_dict
# # # Create your views here.
# # # p_data={'active1':True,
# # #         'active2':False,
# # # 'active3':None}

# # # j_data=json.dumps(p_data)
# # # print(type(p_data))
# # # print(j_data)
# # # print(type(j_data))

# # # j2_data='''{"active1":true,
# # # "active2":false,"active3":null}'''

# # # p2_data=json.loads(j2_data)
# # # print(p2_data)
# # # print(type(p2_data))

# # # @csrf_exempt
# # # def listt(req):
# # #     # if req.method=='POST':
# # #     #     data=req.body
# # #     #     print(data)
# # #     #     print(type(data))
# # #     #     p_data=json.loads(data)
# # #     #     print(p_data)
# # #     #     print(type(p_data))
# # #     #     name=p_data.get('name')
# # #     #     age=p_data.get('age')
# # #     #     con=p_data.get('con')
# # #     #     print(name,age,con)
# # #     #     Stu.objects.create(name=name,age=age)
# # #         emp_data = Stu.objects.all()
# # #         print(emp_data)
# # #         p_data = list(emp_data.values())
# # #         print(p_data)
# # #         j_data = json.dumps(p_data)
# # #         print(j_data)
# # #         print(type(j_data))
# # #         # return JsonResponse(p_data,safe=False) 
# # #         return HttpResponse(j_data,content_type='application/json')



# # @csrf_exempt
# # def listt(req):
# #     if req.method=='POST':
# #         data = req.body
# #         # print(data)
# #         # print(type(data))
# #         p_data = json.loads(data)
# #         # print(p_data)
# #         # print(type(p_data))
# #         n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('city'),p_data.get('age')
# #         # print(n,e,c,a,sep=',')
# #         Stu.objects.create(name=n,email=e,city=c,age=a)
# #         # p_data['msg']="data created successfully"
# #         # print(p_data)
# #         d={'msg':'object created successfully.......','data':p_data}
# #         j_data = json.dumps(d)
# #         # print(j_data)
# #         # print(type(j_data))
# #         # return HttpResponse(j_data,content_type='application/json')
# #         # emp_data = Stu.objects.all()
# #         # print(emp_data)
# #         # p_data = list(emp_data.values())
# #         # print(p_data)
# #         # j_data = json.dumps(p_data)
# #         # print(j_data)
# #         # print(type(j_data))
# #         # return JsonResponse(j_data,safe=False) 
# #         return HttpResponse(j_data,content_type='application/json')
# #     # emp_data = Stu.objects.all()
# #     # print(emp_data)
# #     # p_data = list(emp_data.values())
# #     # print(p_data)
# #     # j_data = json.dumps(p_data)
# #     # print(j_data)
# #     # print(type(j_data))
# #     # return JsonResponse(j_data,safe=False)


# # # def listt(req):
# # #     emp_data = Stu.objects.all()
# # #     p_data = list(emp_data.values())
# # #     return JsonResponse(p_data,safe=False)

# # @csrf_exempt
# # def detail(req,pk):
# #       s=Stu.objects.get(id=pk)
# #       m_data=model_to_dict(s)
# #       j_data=json.dumps(m_data)
# #     #   return JsonResponse(j_data,safe=False) 
# #       return HttpResponse(j_data,content_type='application/json')



# # # def detail(req, pk):
# # #     emp = Stu.objects.get(pk=pk)
# # #     data = {
# # #             "id": emp.id,
# # #             "name": emp.name,
# # #             "age": emp.age,
# # #         }
# # #     return JsonResponse(data)



# # def home(req):
# #     return render(req,'home.html')


# from django.shortcuts import render
# from django.http import JsonResponse,HttpResponse

# from .models import Stu
# import json
# from django.views.decorators.csrf import csrf_exempt
# from django.forms.models import model_to_dict


# @csrf_exempt
# def listt(req):
#     if req.method=='POST':
#         data = req.body
#         # print(data)
#         # print(type(data))
#         p_data = json.loads(data)
#         # print(p_data)
#         # print(type(p_data))
#         n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('city'),p_data.get('age')
#         # print(n,e,c,a,sep=',')
#         Stu.objects.create(name=n,email=e,city=c,age=a)
#         # p_data['msg']="data created successfully"
#         # print(p_data)
#         d={'msg':'object created successfully.......','data':p_data}
#         j_data = json.dumps(d)
#         # print(j_data)
#         # print(type(j_data))
#         return HttpResponse(j_data,content_type='application/json')

#     emp_data = Stu.objects.all()   
#     print(emp_data)
#     p_data = list(emp_data.values())
#     print(p_data)
#     j_data = json.dumps(p_data)
#     print(j_data)
#     print(type(j_data))
#     # return JsonResponse(j_data,safe=False) 
#     return HttpResponse(j_data,content_type='application/json')

# @csrf_exempt
# def detail(req,pk):
#     user = Stu.objects.filter(id=pk)
#     if user:
#         if req.method=='PUT':
#             data = req.body
#             p_data = json.loads(data)
#             n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('city'),p_data.get('age')
#             # if n and e and c and a:
#             if 'name' in p_data and 'email' in p_data and 'city' in p_data and 'age' in p_data:
#                 old_obj = Stu.objects.get(id=pk)
#                 old_obj.name = n
#                 old_obj.email = e 
#                 old_obj.contact = c
#                 old_obj.age = a
#                 old_obj.save()
#                 d={'msg':'Object updated successfully.........'}
#                 j_data = json.dumps(d)
#                 return HttpResponse(j_data,content_type='application/json')
#             else:
#                 d={'msg':'Some required filelds are missing'}
#                 j_data = json.dumps(d)
#                 return HttpResponse(j_data,content_type='application/json')

#         elif req.method=='PATCH':
#             data = req.body
#             p_data = json.loads(data)
#             if p_data:
#                 # p_data = json.loads(data)
#                 n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('city'),p_data.get('age')
#                 old_obj = Stu.objects.get(id=pk)
#                 if 'name' in p_data:
#                     old_obj.name = n
#                 if 'email' in p_data:
#                     old_obj.email = e
#                 if 'city' in p_data:
#                     old_obj.contact = c
#                 if 'age' in p_data:
#                     old_obj.age = a
#                 old_obj.save()
#                 d={'msg':'Object partially updated successfully.........'}
#                 j_data = json.dumps(d)
#                 return HttpResponse(j_data,content_type='application/json')
#             else:
#                 d={'msg':'We need atleast one field to update but we don"t provide '}
#                 j_data = json.dumps(d)
#                 return HttpResponse(j_data,content_type='application/json')

#         elif req.method=='DELETE':
#             old_obj = Stu.objects.get(id=pk)
#             old_obj.delete()
#             d={'msg':'Object deleted successfully........!'}
#             j_data = json.dumps(d)
#             return HttpResponse(j_data,content_type='application/json')
#         emp_data = Stu.objects.get(id=pk)
#         p_data = model_to_dict(emp_data)
#         j_data = json.dumps(p_data)

#         return HttpResponse(j_data,content_type='application/json')
#     else:
#         d={'msg':'Given id is not present in our database'}
#         j_data = json.dumps(d)
#         return HttpResponse(j_data,content_type='application/json')
    

# def stu(req):
#     j_stu=req.body
#     p_data=json.loads(j_stu)
#     pk=p_data.id
#     # if 'id' in p_data:
#     if 'pk':
#         if req.method=='PUT':
#             n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('city'),p_data.get('age')
#             # if n and e and c and a:
#             if 'name' in p_data and 'email' in p_data and 'city' in p_data and 'age' in p_data:
#                 old_obj = Stu.objects.get(id=pk)
#                 old_obj.name = n
#                 old_obj.email = e 
#                 old_obj.contact = c
#                 old_obj.age = a
#                 old_obj.save()
#                 d={'msg':'Object updated successfully.........'}
#                 j_data = json.dumps(d)
#                 return HttpResponse(j_data,content_type='application/json')
#             else:
#                 d={'msg':'Some required filelds are missing'}
#                 j_data = json.dumps(d)
#                 return HttpResponse(j_data,content_type='application/json')

#         elif req.method=='PATCH':
#             if p_data:
#                 # p_data = json.loads(data)
#                 n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('city'),p_data.get('age')
#                 old_obj = Stu.objects.get(id=pk)
#                 if 'name' in p_data:
#                     old_obj.name = n
#                 if 'email' in p_data:
#                     old_obj.email = e
#                 if 'city' in p_data:
#                     old_obj.contact = c
#                 if 'age' in p_data:
#                     old_obj.age = a
#                 old_obj.save()
#                 d={'msg':'Object partially updated successfully.........'}
#                 j_data = json.dumps(d)
#                 return HttpResponse(j_data,content_type='application/json')
#             else:
#                 d={'msg':'We need atleast one field to update but we don"t provide '}
#                 j_data = json.dumps(d)
#                 return HttpResponse(j_data,content_type='application/json')

#         elif req.method=='DELETE':
#             old_obj = Stu.objects.get(id=pk)
#             old_obj.delete()
#             d={'msg':'Object deleted successfully........!'}
#             j_data = json.dumps(d)
#             return HttpResponse(j_data,content_type='application/json')
#         emp_data = Stu.objects.get(id=pk)
#         p_data = model_to_dict(emp_data)
#         j_data = json.dumps(p_data)

#         return HttpResponse(j_data,content_type='application/json')
#     else:
#         d={'msg':'Given id is not present in our database'}
#         j_data = json.dumps(d)
#         return HttpResponse(j_data,content_type='application/json')
#     else:
#         if req.method=='POST':
#             n,e,c,a = p_data.get('name'),p_data.get('email'),p_data.get('city'),p_data.get('age')
#             Stu.objects.create(name=n,email=e,city=c,age=a)
#             d={'msg':'object created successfully.......','data':p_data}
#             j_data = json.dumps(d)
#             return HttpResponse(j_data,content_type='application/json')

#     emp_data = Stu.objects.all()   
#     print(emp_data)
#     p_data = list(emp_data.values())
#     print(p_data)
#     j_data = json.dumps(p_data)
#     print(j_data)
#     print(type(j_data))
#     # return JsonResponse(j_data,safe=False) 
#     return HttpResponse(j_data,content_type='application/json')

