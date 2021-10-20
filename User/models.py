from django.db import models
from Admin.models import *
# Create your models here.
class hobbies_tb(models.Model):
    user_id=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    hobby_id=models.ForeignKey(hobby_tb,on_delete=models.CASCADE)
class message_tb(models.Model):
    source=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    message=models.CharField(max_length=100)
    time=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    filter_status=models.CharField(max_length=20,default='pending')
    
class agecustomize_tb(models.Model):
    user_id=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    factor_id=models.ForeignKey(agefactor_tb,on_delete=models.CASCADE)
class customizecountryfactor_tb(models.Model):
    user_id=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    factor_id=models.ForeignKey(seasonfactor_tb,on_delete=models.CASCADE)
class contact_tb(models.Model):
    user_id=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='user_id')
    contact_id=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='contact_id')
    name=models.CharField(max_length=20)
    remarks=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
class blacklist_tb(models.Model):
    user_id=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='blacklistuser_id')
    contact_id=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='blacklistcontact_id')
    name=models.CharField(max_length=20)
    remarks=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    
class trash_tb(models.Model):
    user_id=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    msg_id=models.ForeignKey(message_tb,on_delete=models.CASCADE)
    
