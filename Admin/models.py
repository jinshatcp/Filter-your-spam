from django.db import models

# Create your models here.
class admin_tb(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class hobby_tb(models.Model):
    hobby_name=models.CharField(max_length=20)
    
class country_tb(models.Model):
    country_name=models.CharField(max_length=20)
class state_tb(models.Model):
    country_id=models.ForeignKey(country_tb,on_delete=models.CASCADE)
    state_name=models.CharField(max_length=20)

class register_tb(models.Model):
    
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    country=models.ForeignKey(country_tb,on_delete=models.CASCADE)
    state=models.ForeignKey(state_tb,on_delete=models.CASCADE)
    phone=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class factor_tb(models.Model):
    hobby_id=models.ForeignKey(hobby_tb,on_delete=models.CASCADE)
    factor_name=models.CharField(max_length=20)
    
    

