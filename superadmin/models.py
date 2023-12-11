from django.db import models
from projectapp.models import *


class Banner(models.Model):
	image=models.ImageField(upload_to='banner/')

class Product(models.Model):
	image=models.ImageField(upload_to='product/')
	pname=models.CharField(max_length=255,default='')
	price=models.CharField(max_length=10,default='')
	a_price=models.CharField(max_length=10,default='')


# Create your models here.

# class User_Registration(models.Model):
#     email=models.CharField(max_length=20)
#     password=models.CharField(max_length=20)
#     confirmpassword=models.CharField(max_length=20)
#     profileimage=models.ImageField(upload_to="profile/",default='')


# class Cart(models.Model):
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)
#     register=models.ForeignKey(User_Registration,on_delete=models.CASCADE)
#     qnty=models.IntegerField()
