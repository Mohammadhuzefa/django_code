"""
URL configuration for trp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tp import views

urlpatterns = [
    # path('', admin.site.urls),
    path('home/',views.home,name="home"),
    path('home2/',views.home2,name="home2"),
    path('home3/',views.home3,name="home3"),
    path('home4/',views.home4,name="home4"),
    path('home5/',views.home5,name="home5"),
    path('home6/',views.home6,name="my_render.html"),
    # path('home7/',views.home7,name="my_render.html"),
    # path('home8/',views.home8,name="my_render.html"),
    path('home8/<int:x>/',views.home8,name='my_render.html'),
    path('home9/<slug:x>/',views.home9,name='my_render.html'),
    path('home10/<slug:name>/<slug:clas>/',views.home10,name='my_render.html'),
    path('homejson/',views.homejson,name='homejson'),
    path('re/',views.re,name='re'),
    path('my_redirect1/',views.my_redirect1,name='my_redirect1'), 
    path('my_redirect2/',views.my_redirect2,name='my_redirect2'), 





 













]
