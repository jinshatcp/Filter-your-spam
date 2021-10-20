from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from django.contrib import messages
import datetime,time

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    countries=country_tb.objects.all()
   
    hobbies=hobby_tb.objects.all()
    
    return render(request,'register.html',{'data':countries,'dataa':hobbies})
def getstate(request):
    cid=request.GET['cid']
    states=state_tb.objects.filter(country_id=cid)
    
    return render(request,'getstate.html',{'states':states})
def registerAction(request):
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    address=request.POST['address']
    country=request.POST['country']
    state=request.POST['state']
    phone=request.POST['phone']
    hobby=request.POST.getlist('hobby')
    print(hobby)
    
    
    username=request.POST['username']
    password=request.POST['password']
    user=register_tb(name=name,gender=gender,dob=dob,address=address,country_id=country,state_id=state,phone=phone,username=username,password=password)
    user.save()
    for i in hobby:
        hob=hobby_tb.objects.get(id=i)
        h=hobbies_tb(hobby_id=hob,user_id=user)
        h.save()
        
    messages.add_message(request,messages.INFO,"registerd")
    return redirect('register')
def sendmessage(request):
    user_id=request.session['user_id']
    return render(request,'sendmessage.html',{'data':user_id})
def messageAction(request):
    user_id=request.session['user_id']
    destination=request.POST['des_username']
    check=register_tb.objects.filter(username=destination)
    
    
    if check.count()>0:
        
        subject=request.POST['subject']
        message=request.POST['message']
        date=datetime.date.today()
        time=datetime.datetime.now().strftime("%H:%M")
        msgs=message_tb(source=user_id,destination=destination,subject=subject,message=message,date=date,time=time,status="message_send")
        msgs.save()
        messages.add_message(request,messages.INFO,"msg sent")
    return redirect('sendmessage')
def viewmessage(request):
    user_id=request.session['user_id']
    msg=message_tb.objects.filter(destination=user_id,status__in=['senderdeleted','message_send'])
    return render(request,'inbox.html',{'data':msg})

def outbox(request):
    user_id=request.session['user_id']
    msg=message_tb.objects.filter(source=user_id,status__in=['recieverdeleted','message_send'])
    return render(request,'outbox.html',{'data':msg})
def deletemessage(request,pid,r):
    user_id=request.session['user_id']
    if r =='0':
        p=message_tb.objects.filter(id=pid)
        for value in p:
            status=value.status
            if (status =='senderdeleted'):
                new=message_tb.objects.filter(id=pid).delete()
            else:
                msg=message_tb.objects.filter(id=pid).update(status="recieverdeleted")
        return redirect('viewmessage')
    else:
        p=message_tb.objects.filter(id=pid)
        for value in p:
            status=value.status
            if (status =='recieverdeleted'):
                new=message_tb.objects.filter(id=pid).delete()
            else:
            
                msg=message_tb.objects.filter(id=pid).update(status="senderdeleted")
        return redirect('outbox')
def update(request):
    countries=country_tb.objects.all()
   
    hobbies=hobby_tb.objects.all()
    user_id=request.session['user_id']
    us=register_tb.objects.filter(username=user_id)
    
    
    hob=hobbies_tb.objects.filter(user_id=us[0].id)
    pid=request.session['user_id']
   
    user=register_tb.objects.filter(username=pid)
    print(user)
    return render(request,'profile_update.html',{'data':user,'countries':countries,'hobbies':hobbies,'hob':hob})
    
    
def updateAction(request):
    user_id=request.session['user_id']
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    address=request.POST['address']
    country=request.POST['country']
    state=request.POST['state']
    phone=request.POST['phone']
    hobby=request.POST.getlist('hobby')
    password=request.POST['password']
    user=register_tb.objects.filter(username=user_id).update(name=name,gender=gender,dob=dob,address=address,country=country,state=state,phone=phone,password=password)
    
    us=register_tb.objects.filter(username=user_id)
    hob=hobbies_tb.objects.filter(user_id=us[0].id)
    l=[]
    for i in hob:
        l.append(i.hobby_id_id)
    for j in hobby:
        if not int(j) in l:
            h=hobby_tb.objects.get(id=j)
            hp=hobbies_tb(user_id=us[0],hobby_id=h)
        
            
            hp.save()
    for k in hob:
        if not str(k.hobby_id_id) in hobby:
            h=hobbies_tb.objects.filter(id=k.id).delete()
    messages.add_message(request,messages.INFO,"profile updated")
    return redirect('home')
            
            
       
        
        
        
         
    
def forward(request,pid):
    msg=message_tb.objects.filter(id=pid)
    return render(request,'forward.html',{'data':msg})
def forwardAction(request):
    user_id=request.session['user_id']
    destination=request.POST['des_username']
    check=register_tb.objects.filter(username=destination)
    
    
    if check.count()>0:
        
        subject=request.POST['subject']
        message=request.POST['message']
        date=datetime.date.today()
        time=datetime.datetime.now().strftime("%H:%M")
        msgs=message_tb(source=user_id,destination=destination,subject=subject,message=message,date=date,time=time,status="message_send")
        msgs.save()
        messages.add_message(request,messages.INFO,"msg forwarded")
    return redirect('home')
def reply(request,pid):
    msg=message_tb.objects.filter(id=pid)
    return render(request,'reply.html',{'data':msg})

    
def customize(request):
    user_id=request.session['user_id']
    us=register_tb.objects.filter(username=user_id)
    hob=hobbies_tb.objects.filter(user_id=us[0].id)
    return render('customize.html')
def getfactor(request):
    hid=request.GET['hid']
    factor=factor_tb.object.filter(hobby_id=hid)
    return render(request,'getfactor.html',{'factor':factor})
def customizeAction(request):
    return render('home.html')
    
    

