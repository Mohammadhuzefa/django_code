from django.urls import path
from myapp.views import *

urlpatterns = [
     
    path('Stu_List/', Stu_List.as_view(), name='Stu_list'),
    path('Stu_Detail/<int:pk>/', Stu_Detail.as_view(), name='Stu_Detail')
]