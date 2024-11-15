from django.urls import path
from adminpanel import views

urlpatterns = [
    path('reg',views.reg,name='registration'),
    path('login',views.login_user,name='login_user'),
    path('logout',views.logout_user,name='logout_user'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('change/pass',views.change_password,name='change_pass'),
    path('user_profile',views.user_profile,name='user_profile'),
    # =======================================================================
    path('cat_store',views.category_store,name='cat_store'),
    path('cat_show',views.cat_show,name='cat_show'),
    path('add_product',views.create_product,name='add_product'),
    path('show_product',views.product_show,name='show_product'),
    path('cart_history',views.cart_history,name='cart_history'),
    # =======================================================================
    path('customer_signup',views.Customer_signup,name='customer_signup'),
    path('customer/login',views.customer_login,name='customer_login'),
    # path('customer_admin',views.customer_admin,name='customer_admin'),
    path('customer_logout',views.customer_logout,name='customer_logout')
]