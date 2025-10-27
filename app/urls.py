

from django.urls import path

from .views import  confirmdeletecustomer, supplierslistview,productslistview,addsupplier,addproduct,confirmdeleteproduct,deleteproduct, \
    edit_product_get, edit_product_post, searchsupplier, products_filtered, loginview, loginaction, logoutaction, \
    customerslistview, addcustomer, searchcustomer, deletecustomer


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
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct,),
    path('delete-product/<int:id>/', deleteproduct,),
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
]
