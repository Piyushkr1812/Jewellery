from django.db import models
from superadmin.models import *


# Create your models here.
class Customer(models.Model):
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    R_password=models.CharField(max_length=200,default=' ')
    mobile=models.IntegerField()
    profile_image=models.ImageField(upload_to="profile/",default='')

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    register=models.ForeignKey(Customer,on_delete=models.CASCADE)
    qnty=models.IntegerField()
    tot_price=models.IntegerField(default=0)

class Order(models.Model):
    pname= models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    product_image=models.CharField(max_length=255,default='')
    address= models.CharField(max_length=200)
    pincode= models.CharField(max_length=200)
    mobile_no=models.IntegerField()
    state=models.CharField(max_length=200)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    status=models.IntegerField(default=0)
    payment_method=models.CharField(max_length=200,default='COD')
    payment_status=models.IntegerField(default=0)
    register=models.ForeignKey(Customer,on_delete=models.CASCADE,default=4)
    