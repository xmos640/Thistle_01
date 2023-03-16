
from django.urls import path,include
from main import views

urlpatterns = [path('',views.index),
               path('logout', views.handelLogout, name="handleLogout"),
               path('accounts/',include('allauth.urls')),
               path('products/<int:myid>',views.productview,name="ProductView")
               ]

 
