from django.urls import path
from .views import *
urlpatterns = [
    path('stu_list/', Stu_list.as_view(), name='Stu_list'),
    path('stu_detail/<int:pk>/', Stu_detail.as_view(), name='Stu_Detail')
]