from django.contrib import admin
from django.urls import path

from . import views
urlpatterns =[
    path('adminindex/',views.adminindex,name='adminindex'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('forget_password/',views.forget_password,name='forget_password'),
    path('add_banner',views.add_banner,name='add_banner'),
    path('add_product',views.add_product,name='add_product'),
    path('del_banner/<id>',views.del_banner,name="del_banner"),
    path('del_product/<id>',views.del_product,name="del_product"),

]