from django.urls import path,include
from . import views

urlpatterns = [
    
    path('CartDetails',views.cart_details,name='cartpage'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('dec/<int:product_id>/',views.min_cart,name='dec_cart'),
    path('delete/<int:product_id>/',views.cart_del,name='del_cart')
    

    
]
