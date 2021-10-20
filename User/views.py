from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from django.contrib import messages
import datetime,time
from django.http import JsonResponse

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
    us=register_tb.objects.filter(username=user_id)
    agefactor=agecustomize_tb.objects.filter(user_id=us[0])
    seasonfactor=customizecountryfactor_tb.objects.filter(user_id=us[0])
    hobbyfactor=hobbies_tb.objects.filter(user_id=us[0])
    
    #filtering inbox using age factor
    for factor in agefactor:
        
        msg=message_tb.objects.filter(destination=user_id,filter_status='pending',message__icontains=factor.factor_id.factor_name).exclude(source__in=register_tb.objects.filter(id__in=blacklist_tb.objects.filter(user_id=us[0]).values('contact_id_id')).values('username')).update(filter_status='filtered')
        
    #filter using season country factor
    for factor in seasonfactor:
        msg=message_tb.objects.filter(destination=user_id,filter_status='pending',message__icontains=factor.factor_id.factor_name).exclude(source__in=register_tb.objects.filter(id__in=blacklist_tb.objects.filter(user_id=us[0]).values('contact_id_id')).values('username')).update(filter_status='filtered')
    #filter using hobbyfactor
    for factor in hobbyfactor:
        msg=message_tb.objects.filter(destination=user_id,filter_status='pending',message__icontains=factor.hobby_id.hobby_name).exclude(source__in=register_tb.objects.filter(id__in=blacklist_tb.objects.filter(user_id=us[0]).values('contact_id_id')).values('username')).update(filter_status='filterd')
    
    msg=message_tb.objects.filter(source__in=register_tb.objects.filter(id__in=contact_tb.objects.filter(user_id=us[0]).values('contact_id_id')).values('username'),destination=user_id,filter_status='pending').update(filter_status='filtered')
    msg=message_tb.objects.filter(destination=user_id,status__in=['senderdeleted','message_send'],filter_status='filtered').exclude(id__in=trash_tb.objects.filter(user_id=us[0]).values('msg_id'))
    return render(request,'inbox.html',{'data':msg})

def outbox(request):
    user_id=request.session['user_id']
    
    msg=message_tb.objects.filter(source=user_id,status__in=['recieverdeleted','message_send'])
    return render(request,'outbox.html',{'data':msg})
def deletemessage(request,pid,r):
    user_id=request.session['user_id']
    if r =='0':
        t=trash_tb.objects.filter(id=pid)
        p=message_tb.objects.filter(id=t[0].msg_id_id)
        for value in p:
            status=value.status
            if (status =='senderdeleted'):
                new=message_tb.objects.filter(id=t[0].msg_id_id).delete()
            else:
                msg=message_tb.objects.filter(id=t[0].msg_id_id).update(status="recieverdeleted")
        t.delete()
        return redirect('viewtrash')
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
    print(us)
    hob=hobbies_tb.objects.filter(user_id=us[0].id)
    print(hob)
    return render(request,'customize.html',{'data':hob})
def getfactor(request):
    hid=request.GET['hid']
    factor=factor_tb.objects.filter(hobby_id=hid)
    return render(request,'getfactor.html',{'factor':factor})
def customizeAction(request):
    user_id=request.session['user_id']
    us=register_tb.objects.filter(username=user_id)
    hobby_id=request.POST['hobby']
    hob=hobby_tb.objects.filter(id=hobby_id)
    factor_id=request.POST['factor']
    fact=factor_tb.objects.filter(id=factor_id)
    factor=customize_tb(user_id=us[0],hobby_id=hob[0],factor_id=fact[0])
    factor.save()
    
    return redirect('customize')
def customizeagefactor(request):
    user_id=request.session['user_id']
    us=register_tb.objects.filter(username=user_id)
    age=us[0].dob
    print(age)
    born_year=age.split('-')
    born_year=born_year[0]
    today=datetime.date.today()
    today=str(today).split('-')
    curr_year=today[0]
    print(curr_year)
    agee=int(curr_year)-int(born_year)
    
    
    fact=agefactor_tb.objects.filter(min_age__lte=agee , max_age__gte=agee)
       
    return render(request,'custagefact.html',{'data':fact})
        
   
    
    
   
def agecustAction(request):
    user_id=request.session['user_id']
    us=register_tb.objects.filter(username=user_id)
    factor_id=request.POST['factor']
    fact=factor_tb.objects.filter(id=factor_id)
    factt=agecustomize_tb(user_id=us[0],factor_id=fact[0])
    factt.save()
    messages.add_message(request,messages.INFO,"customized")
    return redirect('home')
    
    
def customizeseasoncountryfactor(request):
    user_id=request.session['user_id']
    us=register_tb.objects.filter(username=user_id)
    country=us[0].country
    state=us[0].state
    today=datetime.date.today()
    print(today)
    today=str(today).split('-')
    curr_month=today[1]
    print(curr_month)
    factor=countryfactor_tb.objects.filter(country_id=country,state_id=state,month=curr_month)
    print(factor)
    return render(request,'custseasoncountryfactor.html',{'data':factor})
def seasonfactAction(request):
    user_id=request.session['user_id']
    us=register_tb.objects.filter(username=user_id)
    
    factor_id=request.POST['factor']
    fact=seasonfactor_tb.objects.filter(id=factor_id)
    
    factt=customizecountryfactor_tb(user_id=us[0],factor_id=fact[0])
    factt.save()
    return render(request,'home.html')
def addcontact(request):
    user_id=request.session['user_id']
    us=register_tb.objects.filter(username=user_id)
    contact=register_tb.objects.all()
    return render(request,'addcontact.html',{'data':us,'data1':contact})
def contactAction(request):
    username=request.POST['username']
    contacts=register_tb.objects.filter(username=username)
    cont=contacts[0].id
    cts=contact_tb.objects.filter(contact_id=cont)
    if cts.count()>0:
        messages.add_message(request,messages.INFO,"contact already exist")
        return redirect('addcontact')
    else:
        user_id=request.session['user_id']
        us=register_tb.objects.filter(username=user_id)
        name=request.POST['contact_name']
        remark=request.POST['remark']
        date=datetime.date.today()
        time=datetime.datetime.now().strftime("%H:%M")
        contact=contact_tb(name=name,remarks=remark,date=date,time=time,user_id=us[0],contact_id=contacts[0])
        contact.save()
        return render(request,'home.html')
    
        
        
def checkusername(request):
    username=request.GET['username']
    username=register_tb.objects.filter(username=username)
    if username.count() >0:
        check='exist'
    else:
        check='not exist'
    return JsonResponse({'check':check})
def addtoblacklist(request):
    return render(request,'blacklist.html')
def blacklistAction(request):
    
    username=request.POST['username']
    contacts=register_tb.objects.filter(username=username)
    if contacts.count()>0:
        user_id=request.session['user_id']
        us=register_tb.objects.filter(username=user_id)
        name=request.POST['contact_name']
        remark=request.POST['remark']
        date=datetime.date.today()
        time=datetime.datetime.now().strftime("%H:%M")
        contact=blacklist_tb(name=name,remarks=remark,date=date,time=time,user_id=us[0],contact_id=contacts[0])
        contact.save()
        return render(request,'home.html')
    else:
        
        return render(request,'blacklist.html')
def viewcontact(request):
    user_id=request.session['user_id']
    us=register_tb.objects.filter(username=user_id)
    contacts=contact_tb.objects.filter(user_id=us[0])
    return render(request,'mycontacts.html',{'data':contacts})
def viewblacklist(request):
    user_id=request.session['user_id']
    us=register_tb.objects.filter(username=user_id)
    contacts=blacklist_tb.objects.filter(user_id=us[0])
    return render(request,'viewblacklist.html',{'data':contacts})
def block(request,pid):
    user_id=request.session['user_id']
    us=register_tb.objects.filter(username=user_id)
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    contact=contact_tb.objects.filter(id=pid)
    block=blacklist_tb(name=contact[0].name,remarks=contact[0].remarks,date=date,time=time,user_id=contact[0].user_id,contact_id=contact[0].contact_id)
    block.save()
    contact=contact_tb.objects.filter(id=pid).delete()
    contacts=contact_tb.objects.filter(user_id=us[0])
    return render(request,'mycontacts.html',{'data':contacts})
    
def unblock(request,pid):
    user_id=request.session['user_id']
    us=register_tb.objects.filter(username=user_id)
    unblock=blacklist_tb.objects.filter(id=pid).delete()
    block=blacklist_tb.objects.filter(user_id=us[0])
    return render(request,'viewblacklist.html',{'data':block})
def trashAction(request):
    user_id=request.session['user_id']
    us=register_tb.objects.filter(username=user_id)
    msg_id=request.POST.getlist('trash')
    for i in msg_id:
        msg=message_tb.objects.filter(id=i)
        trash_item=trash_tb(user_id=us[0],msg_id=msg[0])
        
        trash_item.save()
    messages.add_message(request,messages.INFO,"moved to trash")
    return redirect('viewmessage')
    
def viewtrash(request):
    user_id=request.session['user_id']
    us=register_tb.objects.filter(username=user_id)
    trash=trash_tb.objects.filter(user_id=us[0])
    return render(request,'viewtrash.html',{'data':trash})
def deletetrash(request,pid):
    dele=trash_tb.objects.filter(id=pid).delete()
    user_id=request.session['user_id']
    us=register_tb.objects.filter(username=user_id)
    trash=trash_tb.objects.filter(user_id=us[0])
    return render(request,'viewtrash.html')
def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    else:
        del request.session['admin_id']
    return render(request,'index.html')
def forgotpassword(request):
    return render(request,'forgotpassword.html')
def checkAction(request):
    name=request.POST['name']
    username=request.POST['username']
    phone=request.POST['phone']
    dob=request.POST['dob']
    select=register_tb.objects.filter(name=name,username=username,phone=phone,dob=dob)
    print (select.count())
    if select.count()>0:
        return render(request,'changepassword.html',{'data':select})
    else:
        return render(request,'login.html',{'msg':"incorrect details"})
def reset(request,pid):
    password1=request.POST['password1']
    password2=request.POST['password2']
    if password1 == password2:
        user=register_tb.objects.filter(id=pid).update(password=password1)
        return render(request,'login.html')
    else:
        return render(request,'changepassword.html',{'msg':"password doesn't match "})
    
def resetpassword(request):
    user_id=request.session['user_id']
    us=register_tb.objects.filter(username=user_id)
    return render(request,'resetpassword.html',{'data':us})
def reset(request):
    password=request.POST['password']
    user_id=request.session['user_id']
    us=register_tb.objects.filter(username=user_id,password=password)
    if us.count()>0:
        password1=request.POST['password1']
        password2=request.POST['password2']
        select=register_tb.objects.filter(id=us[0].id,password=password).update(password=password1)
        return render(request,'home.html')
    else:
        messages.add_message(request,messages.INFO,"incorrect password")
        return redirect('resetpassword')
def viewspam(request):
    user_id=request.session['user_id']
    msg=message_tb.objects.filter(destination=user_id,filter_status='pending',status__in=['senderdeleted','message_send'])
    return render(request,'inbox.html',{'data':msg})
    
