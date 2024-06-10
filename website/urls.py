from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('placeOrder/<str:i>/',views.placeOrder,name='placeOrder'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('register/',views.registerPage,name='register'),
    path('addProduct/',views.addProduct,name='addProduct'),
]


 
