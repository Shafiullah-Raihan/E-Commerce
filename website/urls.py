from django.urls import path
from website import views

urlpatterns = [
    path('',views.index,name='website_home'),
    path('about',views.about,name='about'),
    path('addToCart/<int:id>',views.add_to_carts,name='addToCart'),
    path('cartList',views.cartList,name='cartList'),
    path('cart_delete/<int:id>',views.cart_delete,name='cart_delete'),
    path('cart/Update/<int:id>',views.cart_update,name='cart_update'),
    path('checkout',views.checkout_cart,name='checkout_cart')
]