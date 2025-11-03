

from django import views
from django.urls import path

from .views import  confirmdeletecustomer, supplierslistview,productslistview,addsupplier,addproduct,confirmdeleteproduct,deleteproduct, \
    edit_product_get, edit_product_post, searchsupplier, products_filtered, loginview, loginaction, logoutaction, \
    customerslistview, addcustomer, searchcustomer, deletecustomer, order_list, addorder, delete_order, customer_orders


urlpatterns = [
    # Landing page after login
    
    #path('landing/', landingview),
    

    # Login and logout URLs
    path('', loginview,),
    path('login/', loginaction,),
    path('logout/', logoutaction,),

    # Product URLs
    path('products/', productslistview, name='productslistview'),
    path('add-product/', addproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct,name='confirmdeleteproduct'),
    path('delete-product/<int:id>/', deleteproduct,name='deleteproduct'),
    path('edit-product-get/<int:id>/', edit_product_get, name='edit_product_get'),
    path('edit-product-post/<int:id>/', edit_product_post, name='edit_product_post'),
    path('products-by-supplier/<int:id>/', products_filtered, name='products_filtered'),

    # Supplier URLs
    path('suppliers/', supplierslistview),
    path('add-supplier/', addsupplier),
    path('search-supplier/', searchsupplier),

    # Customer URLs
    path('customers/', customerslistview, name='customerslistview'),
    path('add-customer/', addcustomer, name='addcustomer'),
    path('search-customer/', searchcustomer, name='searchcustomer'),
    path('delete-customer/<int:id>/', deletecustomer, name='deletecustomer'),
    path('confirm-delete-customer/<int:id>/', confirmdeletecustomer, name='confirmdeletecustomer'),

    # Order URLs
    path('orders/', order_list, name='order_list'),
    path('add-order/<int:customer_id>/', addorder, name='addorder'),
    path('delete-order/<int:id>/', delete_order, name='delete_order'),
    path('customer-orders/<int:customer_id>/',customer_orders, name='customer_orders'),

    

]
