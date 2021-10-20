from django.shortcuts import render,redirect
from Admin.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')
def loginAction(request):
    
    log=request.POST['log']
    username=request.POST['username']
    password=request.POST['password']
    if(log=='1'):
        admin=admin_tb.objects.filter(username=username,password=password)
        if admin.count()>0:
            request.session['admin_id']=admin[0].id
            return render(request,'admin_home.html')
        else: 
            
            return render(request,'login.html',{'msg':"incorrect password"})
    else:
        user=register_tb.objects.filter(username=username,password=password)
        if user.count()>0:
            request.session['user_id']=user[0].username
            
            return render(request,'home.html')
        else:
            return render(request,'login.html',{'msg':"incorrect password"})
             
             
        
        
def addHobby(request):
    return render(request,'add_hobby.html')
def hobbyAction(request):
    hobby=request.POST['hobby']
    hobbies=hobby_tb(hobby_name=hobby)
    hobbies.save()
    messages.add_message(request,messages.INFO,"Added Successfully")
    return redirect('addHobby')
def addHobbyfactor(request):
    hobby=hobby_tb.objects.all()
    return render(request,'hobbyfactor.html',{'data':hobby})
def factorAction(request):
    hobby=request.POST['hobby']
    factor=request.POST['factor']
    fact=factor_tb(hobby_id_id=hobby,factor_name=factor)
    fact.save()
    return render(request,'admin_home.html')
