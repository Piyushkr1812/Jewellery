from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from projectapp.models import *
from django.contrib import messages

# Create your views here.
def adminindex(request):
    return render(request,'user/adminindex.html')

def adminlogin(request):
    return render(request,'user/adminlogin.html')

def forget_password(request):
    return render(request,'user/forget_password.html')

def add_banner(request):
    if request.method == "POST":
        bimage=request.FILES['bimage']
        Banner.objects.create(image=bimage)
        return redirect('add_banner')
    else:
        banner=Banner.objects.all()
        data={'banner':banner,'title':"Banner | Admin"}
        return render(request,'user/banner.html',data)   
    
def add_product(request):
    if request.method == "POST":
       image=request.FILES['image']
       pname=request.POST['pname']
       price=request.POST['price']
       a_price=request.POST['a_price']
       Product.objects.create(image=image,pname=pname,price=price,a_price=a_price)
       return redirect('add_product') 
    else:
        products=Product.objects.all()
        data={'product':products,'title':"Product | Admin"}
        return render(request,'user/product.html',data)

def del_banner(request,id):
    check=Banner.objects.get(id=id)
    check.delete()
    return redirect('add_banner')

def del_product(request,id):
    check=Product.objects.get(id=id)
    check.delete()
    return redirect('add_product')

def Order(request):
    data={'title':'cart'}
    if request.method == "POST":
        if request.session['userid'] != '':
            pid=request.POST['pid']
            uid=request.session['userid']
            cart.objects.create(product_id=pid,register_id=uid,qnty=1)
            return redirect('product') 
        else:
            cart=cart.objects.all()
            data={'cart':cart}
            return render(request,'cart.html',data) 
    else:
        return render(request,'cart.html',data)