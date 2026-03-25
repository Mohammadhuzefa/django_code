from django.urls import path
from myapp import views

urlpatterns = [
    path('stu_list/',views.stu_list),
    path('stu_details/<int:pk>/',views.stu_details),
]