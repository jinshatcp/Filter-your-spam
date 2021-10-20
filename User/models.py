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
    
