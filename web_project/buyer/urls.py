from  django.urls import path
from  .views import *


urlpatterns = [
    path('',index, name='index'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('cycle/',cycle, name='cycle'),
    path('news/',news, name='news'),
    path('add_row/',add_row, name='add_row'),
    path('register/',register, name='register'),
    path('login/',login,name='login'),
    path('otp/',otp, name='otp'),
    path('cart/',cart, name='cart'),
    path('logout/',logout, name='logout'),
    path('paymentfail/',paymentfail, name='paymentfail'),
    path('paymentsuccess/',paymentsuccess, name='paymentsuccess'),
    path('add_to_cart/<int:pk>',add_to_cart,name='add_to_cart'), 
    path('del_cart_item/<int:c_item>',del_cart_item,name='del_cart_item'),
    path('cart/paymenthandler/', paymenthandler, name='paymenthandler')
]