from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import View

from app.forms import *

# Create your views here.

# Function Based Views

def Fbv_String(request):
    return HttpResponse('Function based View')

#Class Based Views

class Cbv_String(View):
    def get(self,request):
        return HttpResponse('class based view')
    
#Funnction Based Html Page

def Fb_html(request):
    return render(request,'Fb_html.html')

#Class Based Html Page

class Cb_html(View):
    def get(self,request):
        return render(request,'Cb_html.html')
    
#Funnction Based Forms Page

def FB_Forms(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Data inserted successfully..!!')
    
    return render(request,'FB_Forms.html',d)

#class based form page

class Cb_Form(View):
    def get(self,request):
        TFO=TopicForm()
        d={'TFO':TFO}
        return render(request,'CBV_form.html',d)
    
    def post(self, request):
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted')


        
    

    

