"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.landingpage, name='landingpage')
    # path('landing/',views.landingpage, name='landingpage')
    # path('landing',views.landingpage, name='landingpage')
    # path('json_response/',views.json_response,name='json_response')
    # path('download_csv/',views.download_csv,name='download_csv')
    path('my_redirect1/',views.my_redirect1,name='my_redirect1'),
    path('my_redirect2/',views.my_redirect2,name='my_redirect2'),
]
