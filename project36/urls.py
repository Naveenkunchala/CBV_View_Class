"""project36 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Fbv_String/',Fbv_String,name='Fbv_String'),
    path('Cbv_String/',Cbv_String.as_view(),name='Cbv_String'),
    path('Fb_html/',Fb_html,name='Fb_html'),
    path('Cb_html/',Cb_html.as_view(),name='Cb_html'),
    path('FB_Forms/',FB_Forms,name='FB_Forms'),
    path('Cb_Form/',Cb_Form.as_view(),name='Cb_Form')
    
]
