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
    if(log == '1'):
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
             
             
def adminhome(request):
    
     return render(request,'admin_home.html')      
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
def addAgefactor(request):
    return render(request,'agefactor.html')
def agefactorAction(request):
    minage=request.POST['minage']
    maxage=request.POST['maxage']
    factor_name=request.POST['factname']
    agefact=agefactor_tb(min_age=minage,max_age=maxage,factor_name=factor_name)
    agefact.save()
    return render(request,'admin_home.html')
        
def addseason(request):
    return render(request,'addseason.html')
def seasonAction(request):
    season=request.POST['season']
    ses=season_tb(season_name=season)
    ses.save()
    messages.add_message(request,messages.INFO,"season added")
    return redirect('addseason')
def addseasonfactor(request):
    season=season_tb.objects.all()
    return render(request,'addseasonfactor.html',{'data':season})

def seasonfactorAction(request):
    season=request.POST['season']
    factor=request.POST['factor']
    fact=seasonfactor_tb(season_id_id=season,factor_name=factor)
    fact.save()
    messages.add_message(request,messages.INFO,"season factor added")
    
    return redirect('addseasonfactor')
def addseasoncountryfactor(request):
    ses=season_tb.objects.all()
    return render(request,'seasoncountryfactor.html',{'data':ses})
def getfact(request):
    sid=request.GET['sid']
    factor=seasonfactor_tb.objects.filter(season_id=sid)
    
    return render(request,'getfactor.html',{'factor':factor})
def countryAction(request):
    season=request.POST['season']
    season=season_tb.objects.filter(id=season)
    
    factor=request.POST['factor']
    factor=seasonfactor_tb.objects.filter(id=factor)
    country=request.POST['country']
    state=request.POST['state']
    month=request.POST['month']
    con=countryfactor_tb(month=month,season_id=season[0],factor_id=factor[0],country_id=country,state_id=state)
    con.save()
    return redirect('addseasoncountryfactor')
    
