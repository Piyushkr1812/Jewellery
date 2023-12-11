from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from superadmin.models import *
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello this is django class</h1>')

def about(request):
    data={'title':'about'}
    return HttpResponse('This page belongs to about')

def shop(request):
    # data={'title':'shop'}
    product=Product.objects.all()
    data={'product':product}
    return render(request,'shop.html',data)

def contact(request):
    data={'title':'contact'}
    return render(request,'contact.html',data)


def ring(request):
    data={'title':'ring'}
    return render(request,'product/ring.html',data)

def earing(request):
    data={'title':'earing'}
    return render(request,'product/earing.html',data)

def chain(request):
    data={'title':'chain'}
    return render(request,'product/chain.html',data)

def bracelets(request):
    data={'title':'bracelets'}
    return render(request,'product/bracelets.html',data)

def pendents(request):
    data={'title':'pendants'}
    return render(request,'product/pendents.html',data)

def neclaces(request):
    data={'title':'neclaces'}
    return render(request,'product/neclaces.html',data)

def mangalsutra(request):
    data={'title':'mangalsutra'}
    return render(request,'product/mangalsutra.html',data)

def bangles(request):
    data={'title':'bangles'}
    return render(request,'product/bangles.html',data)

def gemstone(request):
    data={'title':'gemstone'}
    return render(request,'product/gemstone.html',data)

def register(request):
    data={'title':'register'}
    if request.method=="POST":

        password=request.POST['password']

        username=request.POST['username']

        mobile=request.POST['mobile']

        email=request.POST['email']
        R_password=request.POST['R_password']
        if R_password==password:
            email_check=Customer.objects.filter(email=email).first()
            if email_check is not None:
                messages.add_message(request,messages.ERROR,"This Email Id already registered!!")
                return redirect('register')

            else:
                check=Customer.objects.create(email=email,password=password,mobile=mobile,username=username,R_password=R_password)
                # return HttpResponse("Registration Sucessfull")
                messages.add_message(request,messages.SUCCESS,"Registration Successfull!!")
                # return HttpResponse("Already Exist This Email")
                return redirect('register')
        else:
            # return HttpResponse('Check Password')
            messages.add_message(request,messages.ERROR,"Please match password and confirm password!!")
            return redirect('register')
    return render(request,'login.html')

def login(request):
    data={'title':'login'}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        check=Customer.objects.filter(username=username,password=password).first()
        if check is not None:
            request.session['username']=username
            # return HttpResponse(check.id)
            request.session['userid']=check.id
            # return HttpResponse(check.id)
            # return HttpResponse('Login successfully!!')
            messages.add_message(request,messages.SUCCESS,"Login Successfully!!")
            return redirect('index')
        else:
            # return HttpResponse('Invalid credentials!!')
            messages.add_message(request,messages.ERROR,"Invalid Credentials!!")
            return redirect('register')
    return redirect('register')


def shop_details(request):
    uid=request.session['userid']
    order=Order.objects.filter(register_id=uid)
    data={'title':'shop_details','order':order}
    return render(request ,'shop_details.html',data)

def index(request):
    banner_data=Banner.objects.all()
    data={'banner':banner_data}
    return render(request ,'index.html',data)

def Edit_profile(request):
    data={'title':'Edit_profile'}
    if 'userid' in request.session:
        if request.method == "POST":
            mobile=request.POST['mobile']
            username=request.POST['username']
            password=request.POST['password']
            email=request.POST['email']
            profile_image=request.FILES['profile_image']
            data=Customer.objects.get(id=request.session['userid'])
            data.mobile=mobile
            data.username=username
            data.password=password
            data.email=email
            data.profile_image=profile_image
            data.save()
            messages.add_message(request,messages.SUCCESS,"Profile Update Sucessful!!")
            return redirect('profile')
        else:
            profile=Customer.objects.get(id=request.session['userid'])
            data={'profile':profile,'title':'Edit profile'}
            return render (request,'edit_profile.html',data)
    else:
        messages.add_message(request,messages.ERROR,"Please Login First!!")
        return redirect('login')


def logout(request):
    del request.session['userid']
    del request.session['username']
    # return HttpResponse('Logout Successfull')
    messages.add_message(request,messages.SUCCESS,"Logout Successfull!!")
    return redirect('index')

def profile(request):
    data={'title':'profile'}
    if 'userid' in request.session:
        profile_data=Customer.objects.get(id=request.session['userid'])
        data={'profile':profile_data}
        return render(request,'profile.html',data)
    else:
        messages.add_message(request,messages.ERROR,'Please Login first!')
        return redirect('login')
    
# def test(request):
#     data={'title':'Home | Company'}
#     return render(request,'test.html',data)

def list(request):
    user_list=Customer.objects.all()
    data={'user_list':user_list}
    return render(request,'list.html',data)
    
def del_user(request,id):
    checkk=Customer.objects.get(id=id)
    checkk.delete()
    messages.add_message(request,messages.SUCCESS,"Delete Successfull!!")
    return redirect('list')
    
def cart(request):
    if request.method == "POST":
        if 'userid' in request.session:
            pid=request.POST['pid']
            uid=request.session['userid']
            Cart.objects.create(product_id=pid,register_id=uid,qnty=1)
            return redirect('product') 
        else:
            uid=request.session['userid']
            cart=Cart.objects.filter(register_id=uid)
            data={'cart':cart}
            return render(request,'cart.html',data) 
    else:
        if 'userid' in request.session:
            uid=request.session['userid']
            cart=Cart.objects.filter(register_id=uid)
            data={'cart':cart}
            return render(request,'cart.html',data)
        return redirect('signin')
    
def product(request):
    product=Product.objects.all()
    data={'product':product}
    return render(request,'shop.html',data)

def checkout(request):
    return render(request ,'checkout.html')

def buynow(request):
    if 'userid' in request.session:
        if request.method == "POST":
            pid=request.POST['pid']
            uid=request.session['userid']
            product=Product.objects.get(id=pid)
            Order.objects.create(register_id=uid,pname=product.pname,price=product.price,status=0,product_image=product.image,mobile_no=0)
            last_id=(Order.objects.latest('id')).id
            data={'title':'buynow','last_id':last_id}
            return render(request,'checkout.html',data)
        else:
            return redirect('product')
    else:
        messages.add_message(request,messages.ERROR,'Please Login first!')
        return redirect('login')    

def order_now(request):
    if 'userid' in request.session:
        if request.method == 'POST':
            order_id =  request.POST['order_id']
            mobile_no = request.POST['mobile_no']
            address = request.POST['address']
            pincode = request.POST['pincode']
            state = request.POST['state']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            payment_method = request.POST['payment_method']
            if(payment_method == 'online'):
                payment_status=0
            else:
                payment_status = 1
            ord = Order.objects.get(id=order_id)
            ord.mobile_no=mobile_no
            ord.address=address
            ord.pincode=pincode
            ord.last_name=last_name
            ord.state=state
            ord.first_name=first_name
            ord.payment_method=payment_method
            ord.payment_status=payment_status
            ord.email=email
            ord.status=1
            ord.save()

            subject = 'Regarding Order'
            message = f'Hi {first_name}, Thank you for order.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email,'admin@gmail.com' ]
            send_mail( subject, message, email_from, recipient_list )


            messages.add_message(request, messages.SUCCESS,"order succesful")
            return redirect('my_order')
        else:
            return redirect('product')
    else:
        messages.add_message(request, messages.ERROR,"login first")
        return render(request,'shop_details.html') 
    
def my_order(request):
    uid = request.session['userid']
    ord = Order.objects.filter(register_id=uid)
    data={'title':'My Order','order':ord}
    return render(request,'shop_details.html',data)

def upd_qnty(request,id):
    if request.method == "POST":
        qnty=request.POST['qnty']
        data=Cart.objects.get(id=id)
        tot_price=int(data.product.price)*int(qnty)
        data.tot_price=tot_price
        data.qnty=qnty
        data.save()
        return redirect('cart')
    return redirect('cart')

def remove_cart_prod(request,id):
    data=Cart.objects.get(id=id)
    data.delete()
    return redirect('cart')