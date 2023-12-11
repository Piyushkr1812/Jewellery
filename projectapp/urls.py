from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('', views.home, name='home')
    path('paras', views.home, name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('shop',views.shop,name='shop'),
    path('register',views.register,name='register'),
    path('shop_details',views.shop_details,name='shop_details'),
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('ring',views.ring,name='ring'),
    path('earing',views.earing,name='earing'),
    path('chain',views.chain,name='chain'),
    path('bracelets',views.bracelets,name='bracelets'),
    path('pendents',views.pendents,name='pendents'),
    path('neclaces',views.neclaces,name='neclaces'),
    path('bangles',views.bangles,name='bangles'),
    path('mangalsutra',views.mangalsutra,name='mangalsutra'),
    path('gemstone',views.gemstone,name='gemstone'),

    # path('test',views.test,name='test'),
    path('Edit_profile',views.Edit_profile,name='Edit_profile'),
    path('list',views.list,name='list'),
    path('del_user/<id>',views.del_user,name="del_user"),
    path('product',views.product,name='product'),
    path('cart',views.cart,name='cart'),
    path('buynow',views.buynow,name='buynow'),
    path('checkout',views.checkout,name='checkout'),
    path('order_now',views.order_now,name='order_now'),
    path('my_order',views.my_order,name='my_order'),
    path('upd_qnty/<id>',views.upd_qnty,name='upd_qnty'),
    path('remove_cart_prod/<id>',views.remove_cart_prod,name='remove_cart_prod'),
    # path('cart_total',views.cart_total,name='cart_total'),
]
