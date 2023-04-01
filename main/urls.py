
from django.urls import path,include
from main import views

urlpatterns = [path('',views.index),
               path('logout', views.handelLogout, name="handleLogout"),
               path('accounts/',include('allauth.urls')),
               path('products/<int:myid>',views.productview,name="ProductView"),
               path('orders/order-id:gikud781<int:myid>',views.orderview,name="orderView"),
               path('cart/',views.cart,name='cart'),
               path('checkout/',views.checkout,name='checkout'),
               path('orders/',views.orders,name='orders')
               
               ]

 
